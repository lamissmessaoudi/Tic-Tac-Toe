__authors__ = "Messaoudi Lamiss"

"""
Ce fichier permet de définir la classe Plateau permettant de jouer au jeu Tic-Tac-Toe
Cette classe permet d'initialiser le plateau de jeu , l'afficher, vérifier s'il est plein ou pas, vérifier si une position est valide pour jouer
choisir la prochaine case pour l'ordinateur à jouer ,  vérifier si une joueur a gagner, est valide pour jouer

"""

from case import Case
from random import randrange


class Plateau:
    """
    Classe modélisant le plateau du jeu Tic-Tac-Toe.

    Attributes:
        cases (dictionary): Dictionnaire de cases. La clé est une position (ligne, colonne),
                            et la valeur est une instance de la classe Case.
    """

    def __init__(self):
        """
        Méthode spéciale initialisant un nouveau plateau contenant les 9 cases du jeu.
        """

        # Dictionnaire de cases.
        # La clé est une position (ligne, colonne), et la valeur est une instance de la classe Case.
        self.cases = {}

        # Appel d'une méthode qui initialise un plateau contenant des cases vides.
        self.initialiser()

    def initialiser(self):
        """
        Méthode fournie permettant d'initialiser le plateau avec des cases vides (contenant des espaces).
        """

        # Vider le dictionnaire (pratique si on veut recommencer le jeu).
        self.cases.clear()
        # Parcourir le dictionnaire et mettre des objets de la classe Case.
        # dont l'attribut "contenu" serait un espace (" ").
        for i in range(0, 3):
            for j in range(0, 3):
                self.cases[i, j] = Case(" ")

    def __str__(self):
        """Méthode spéciale fournie indiquant à Python comment représenter une instance de Plateau
        sous la forme d'une chaîne de caractères. Permet donc d'afficher le plateau du jeu
        à l'écran en faisant par exemple:
        p1 = Plateau()
        print(p1)
        Donc, lorsque vous affichez un objet, Python invoque automatiquement la méthode __str__
        Voici un exemple d'affichage:
         +-0-+-1-+-2-+
        0|   | X | X |
         +---+---+---+
        1| O | O | X |
         +---+---+---+
        2|   |   | O |
         +---+---+---+

        Returns:
            string: Retourne la chaîne de caractères à afficher.
        """
        s = " +-0-+-1-+-2-+\n"
        for i in range(0, 3):
            s += str(i) + "| "
            for j in range(0, 3):
                s += self.cases[(i, j)].contenu + " | "
            if i <= 1:
                s += "\n +---+---+---+\n"
            else:
                s += "\n +---+---+---+"
        return s

    def non_plein(self):
        """
        Retourne si le plateau n'est pas encore plein.
        Il y a donc encore des cases vides (contenant des espaces et non des "X" ou des "O").

        Returns:
            bool: True si le plateau n'est pas plein, False autrement.
        """
        # pass
        # mon travail
        # si on trouve un espace dans le plateau , il n'est pas plein ==> true
        b = False
        for i in range(0, 3):
            for j in range(0, 3):
                if self.cases[(i, j)].contenu == " ":
                    b = True
        return b

    def position_valide(self, ligne, colonne):
        """
        Vérifie si une position est valide pour jouer.
        La position ne doit pas être occupée.
        Il faut utiliser la méthode est_vide() de la classe Case.

        Args:
            ligne (int): Le numéro de la ligne dans le plateau du jeu.
            colonne (int): Le numéro de la colonne dans le plateau du jeu.

        Returns:
            bool: True si la position est valide, False autrement.
        """
        assert isinstance(ligne, int), "Plateau: ligne doit être un entier."
        assert isinstance(colonne, int), "Plateau: colonne doit être un entier."

        # pass
        # mon travail
        # il faut que le num de ligne et de colonne soit compris entre 0 et 2
        # il faut que le case soit vide ==> contenu de case ==" "

        return ligne < 0 or ligne > 2 or colonne < 0 or colonne > 2 or (self.cases[(ligne, colonne)].est_vide())

    def selectionner_case(self, ligne, colonne, pion):
        """
        Permet de modifier le contenu de la case
        qui a les coordonnées (ligne,colonne) dans le plateau du jeu
        en utilisant la valeur de la variable pion.

        Args:
            ligne (int): Le numéro de la ligne dans le plateau du jeu.
            colonne (int): Le numéro de la colonne dans le plateau du jeu.
            pion (string): Une chaîne de caractères ("X" ou "O").
        """
        assert isinstance(ligne, int), "Plateau: ligne doit être un entier."
        assert isinstance(colonne, int), "Plateau: colonne doit être un entier."
        assert isinstance(pion, str), "Plateau: pion doit être une chaîne de caractères."
        assert pion in ["O", "X"], "Plateau: pion doit être 'O' ou 'X'."

        # pass
        # mon travail
        # si la case est valide on met le pion sinon on affiche le message
        if self.position_valide(ligne, colonne):
            self.cases[(ligne, colonne)].contenu = pion
        else:
            print("*****la case déja occupée***** ")

    def est_gagnant(self, pion):
        """
        Permet de vérifier si un joueur a gagné le jeu.
        Il faut vérifier toutes les lignes, colonnes et diagonales du plateau.

        Args:
            pion (string): La forme du pion utilisé par le joueur en question ("X" ou "O").

        Returns:
            bool: True si le joueur a gagné, False autrement.
        """

        assert isinstance(pion, str), "Plateau: pion doit être une chaîne de caractères."
        assert pion in ["O", "X"], "Plateau: pion doit être 'O' ou 'X'."

        # pass
        # mon travail
        # on vérifie les cases du 1ér diagonale
        if self.cases[(0, 0)].contenu == self.cases[(1, 1)].contenu == self.cases[(2, 2)].contenu == pion:
            return True
        # on vérifie les cases du diagonale inverse
        elif self.cases[(0, 2)].contenu == self.cases[(1, 1)].contenu == self.cases[(2, 0)].contenu == pion:
            return True
        # on vérifie les cases alignés selon la meme ligne ou colonne
        for i in range(0, 3):
            if self.cases[(i, 0)].contenu == self.cases[(i, 1)].contenu == self.cases[(i, 2)].contenu == pion:
                return True
            elif self.cases[(0, i)].contenu == self.cases[(1, i)].contenu == self.cases[(2, i)].contenu == pion:
                return True
        else:
            return False

    def choisir_prochaine_case(self, pion):
        assert isinstance(pion, str), "Plateau: pion doit être une chaîne de caractères."
        assert pion in ["O", "X"], "Plateau: pion doit être 'O' ou 'X'."

        # pass
        # mon travail

        # pion2 un variable qui va contenir le pion de l'adversaire
        if pion == 'X':
            pion2 = 'O'
        else:
            pion2 = 'X'
        # On verifie tout d'abord si on a une chance pour gagner
        # Si on n'a pas une chance pour gagner, on esssaye de bloquer l'adversaire
        # Sinon on choisi une case aléatoire et valide

        # Verification de 1ér diagonale au cas ou il ya chance pour ganger
        if self.cases[(0, 0)].contenu == self.cases[(1, 1)].contenu == pion and self.position_valide(2, 2):
            return 2, 2
        elif self.cases[(0, 0)].contenu == self.cases[(2, 2)].contenu == pion and self.position_valide(1, 1):
            return 1, 1
        elif self.cases[(2, 2)].contenu == self.cases[(1, 1)].contenu == pion and self.position_valide(0, 0):
            return 0, 0
        # verification de diagonale inverse au cas ou il ya chance pour ganger

        elif self.cases[(0, 2)].contenu == self.cases[(2, 0)].contenu == pion and self.position_valide(1, 1):
            return 1, 1
        elif self.cases[(0, 2)].contenu == self.cases[(1, 1)].contenu == pion and self.position_valide(2, 0):
            return 2, 0
        elif self.cases[(2, 0)].contenu == self.cases[(1, 1)].contenu == pion and self.position_valide(0, 2):
            return 0, 2
        else:
            # verification des lignes au cas ou il ya chance pour ganger
            for i in range(0, 3):
                if self.cases[(i, 0)].contenu == self.cases[(i, 1)].contenu == pion and self.position_valide(i, 2):
                    return i, 2
                elif self.cases[(i, 0)].contenu == self.cases[(i, 2)].contenu == pion and self.position_valide(i, 1):
                    return i, 1
                elif self.cases[(i, 1)].contenu == self.cases[(i, 2)].contenu == pion and self.position_valide(i, 0):
                    return i, 0
                # verification des colonnes au cas ou il ya chance pour ganger
                elif self.cases[(0, i)].contenu == self.cases[(2, i)].contenu == pion and self.position_valide(1, i):
                    return 1, i
                elif self.cases[(0, i)].contenu == self.cases[(1, i)].contenu == pion and self.position_valide(2, i):
                    return 2, i
                elif self.cases[(1, i)].contenu == self.cases[(2, i)].contenu == pion and self.position_valide(0, i):
                    return 0, i
        # verification de 1ér diagonale au cas ou il ya chance de bloquer l'adversaire
        if self.cases[(0, 0)].contenu == self.cases[(1, 1)].contenu == pion2 and self.position_valide(2, 2):
            return 2, 2
        elif self.cases[(0, 0)].contenu == self.cases[(2, 2)].contenu == pion2 and self.position_valide(1, 1):
            return 1, 1
        elif self.cases[(2, 2)].contenu == self.cases[(1, 1)].contenu == pion2 and self.position_valide(0, 0):
            return 0, 0
            # verification de diagonale inverse au cas ou il ya chance de de bloquer l'adversaire

        elif self.cases[(0, 2)].contenu == self.cases[(2, 0)].contenu == pion2 and self.position_valide(1, 1):
            return 1, 1
        elif self.cases[(0, 2)].contenu == self.cases[(1, 1)].contenu == pion2 and self.position_valide(2, 0):
            return 2, 0
        elif self.cases[(2, 0)].contenu == self.cases[(1, 1)].contenu == pion2 and self.position_valide(0, 2):
            return 0, 2
        else:
            # verification des lignes  au cas ou il ya chance pour bloquer l'adversaire
            for i in range(0, 3):
                if self.cases[(i, 0)].contenu == self.cases[(i, 1)].contenu == pion2 and self.position_valide(i, 2):
                    return i, 2
                elif self.cases[(i, 0)].contenu == self.cases[(i, 2)].contenu == pion2 and self.position_valide(i, 1):
                    return i, 1
                elif self.cases[(i, 1)].contenu == self.cases[(i, 2)].contenu == pion2 and self.position_valide(i, 0):
                    return i, 0
                # verification des colonnes  au cas ou il ya chance pour bloquer l'adversaire
                elif self.cases[(0, i)].contenu == self.cases[(2, i)].contenu == pion2 and self.position_valide(1, i):
                    return 1, i
                elif self.cases[(0, i)].contenu == self.cases[(1, i)].contenu == pion2 and self.position_valide(2, i):
                    return 2, i
                elif self.cases[(1, i)].contenu == self.cases[(2, i)].contenu == pion2 and self.position_valide(0, i):
                    return 0, pion2
        # Dans le cas ou le plateau est vide
        # Dans le cas ou l'ordinateur ne peut pas gagner pour le moment ou l'adversaire ne  peut pas etre bloquer
        # On choisi une case aléatoire (0,1,2) et valide
        x = randrange(0, 3)
        y = randrange(0, 3)
        while not (self.position_valide(x, y)):
            x = randrange(0, 3)
            y = randrange(0, 3)
        return x, y
