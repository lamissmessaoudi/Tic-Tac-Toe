__authors__ = "Messaoudi Lamiss"


"""Ce fichier permet de définir la classe Jouer permettant de jouer au jeu Tic-Tac-Toe
Cette classe permet de lancer une partie, choisir le mode du jeu, saisir les noms et pions des joueurs, remplir le plateau,
annocer les gagnants , afficher les statistiques et recomencer le jeu   """

from plateau import Plateau
from joueur import Joueur


class Partie:
    """
    Classe modélisant une partie du jeu Tic-Tac-Toe utilisant
    un plateau et deux joueurs (deux personnes ou une personne et un ordinateur).

    Attributes:
        plateau (Plateau): Le plateau du jeu contenant les 9 cases.
        joueurs (Joueur list): La liste des deux joueurs (initialement une liste vide).
        joueur_courant (Joueur): Le joueur courant (initialisé à une valeur nulle: None)
        nb_parties_nulles (int): Le nombre de parties nulles (aucun joueur n'a gagné).
    """

    def __init__(self):
        """
        Méthode spéciale initialisant une nouvelle partie du jeu Tic-Tac-Toe.
        """
        self.plateau = Plateau()  # Le plateau du jeu contenant les 9 cases.
        self.joueurs = []  # La liste des deux joueurs (initialement une liste vide).
        # Au début du jeu, il faut ajouter les deux joueurs à cette liste.
        self.joueur_courant = None  # Le joueur courant (initialisé à une valeur nulle: None)
        # Pendant le jeu et à chaque tour d'un joueur,
        # il faut affecter à cet attribut ce joueur courant.
        self.nb_parties_nulles = 0  # Le nombre de parties nulles (aucun joueur n'a gagné).

    def jouer(self):
        """
        Permet de démarrer la partie en commençant par l'affichage de ce texte:

        Bienvenue au jeu Tic Tac Toe.
        ---------------Menu---------------
        1- Jouer avec l'ordinateur.
        2- Jouter avec une autre personne.
        0- Quitter.
        -----------------------------------
        Entrez s.v.p. un nombre entre 0 et 2:?

        Cette méthode doit donc utiliser la méthode saisir_nombre().
        Elle doit par la suite demander à l'utilisateur les noms des joueurs.
        Veuillez utiliser 'Colosse' comme nom pour l'ordinateur.
        Il faut créer des instances de la classe Joueur et les ajouter à la liste joueurs.
        Il faut utiliser entre autres ces méthodes:
            *- demander_forme_pion(): pour demander au premier joueur la forme de son pion (X ou O).
              (Pas besoin de demander à l'autre joueur ou à l'ordinateur cela, car on peut le déduire).
            *- plateau.non_plein(): afin d'arrêter le jeu si le plateau est plein (partie nulle).
            *- tour(): afin d'exécuter le tour du joueur courant.
            *- plateau.est_gagnant(): afin de savoir si un joueur a gagné et donc arrêter le jeu.
        Il faut alterner entre le premier joueur et le deuxième joueur à chaque appel de tour()
        en utilisant l'attribut joueur_courant.
        Après la fin de chaque partie, il faut afficher les statistiques sur le jeu.
        Voici un exemple:

        Partie terminée! Le joueur gagnant est: Colosse
        Parties gagnées par Mondher : 2
        Parties gagnées par Colosse : 1
        Parties nulles: 1
        Voulez-vous recommencer (O,N)?

        Il ne faut pas oublier d'initialiser le plateau avant de recommencer le jeu.
        Si l'utilisateur ne veut plus recommencer, il faut afficher ce message:
        ***Merci et au revoir !***
        """

        # pass
        # mon travail
        # l'affichage de texte de début
        print("Bienvenue au jeu Tic Tac Toe.\n"
              " ---------------Menu--------------- \n"
              "1- Jouer avec l'ordinateur.\n"
              "2-Jouter avec une autre personne. \n"
              "0- Quitter.\n"
              "-----------------------------------")
        # Appel à la méthode saisir_nombre()pour selectionner le mode du jeu.
        choix = self.saisir_nombre(0, 2)
        if choix == 0:
            # le traitement de mode 0
            # Le programme s’arrête et affiche le message « ***Merci et au revoir !*** »
            print(" ***Merci et au revoir !*** ")
            exit()

        elif choix == 1:
            # le traitement de mode 1

            # Le programme doit commencer une partie entre la personne et l’ordinateur
            # Création des instances de la classe Joueur
            # Création du premier joueur de type personne pour l'utilisateur
            nom = input("Entrez s.v.p. votre nom: ? ")
            p1 = self.demander_forme_pion()

            j1 = Joueur(nom, "Personne", p1)

            # Création du 2émé joueur(ordinateur) dont le nom est Colosse et le pion different à celui de l'autre joueur
            if p1 == "X":
                j2 = Joueur("Colosse", "Ordinateur", "O")
            else:
                j2 = Joueur("Colosse", "Ordinateur", "X")

        elif choix == 2:
            # Traitement du mode 2 :

            # Le programme doit commencer une partie entre 2 personnes et crée 2 joueurs j1 et j2
            # Création du premiere instances de la classe Joueur (j1)
            nom1 = input("Entrez s.v.p. votre nom: ? ")
            pion = self.demander_forme_pion()
            j1 = Joueur(nom1, "Personne", pion)

            # Création du 2émé instances de la classe Joueur(j2)le pion different à celui de l'autre joueur
            nom2 = input("Entrez s.v.p. le nom de l'autre joueur: ? ")
            if pion == "X":
                j2 = Joueur(nom2, "Personne", "O")
            else:
                j2 = Joueur(nom2, "Personne", "X")

        # Ajouter les instances de classe joueurs  à la liste joueurs.
        self.joueurs.append(j1)
        self.joueurs.append(j2)

        # Afficher le plateau
        print(self.plateau.__str__())

        # On alterne les tours entre les 2 joueurs jusqu'à le plateau devient plein ou l'un de joueur gagne
        self.alterner_tour(choix, j1, j2)

        # le plateau est plein ou on a un gagnant

        # la partie est terminée,  on affiche le gagnant (s'il existe) et les statistiques sur le jeu.
        self.partie_terminée(j1, j2)

        x = input("Voulez-vous recommencer (O,N)?")
        while x != "N" and x != "O":
            x = input("Voulez-vous recommencer (O,N)?")

        # L'utilisateur veut recommencer
        # On initialise le plateau et on recommence le jeu.
        while x == "O":
            self.plateau.initialiser()
            self.alterner_tour(choix, j1, j2)
            self.partie_terminée(j1, j2)
            x = input("Voulez-vous recommencer (O,N)?")
            while x != "N" and x != "O":
                x = input("Voulez-vous recommencer (O,N)?")
        if x == 'N':
            # Le programme s’arrête et affiche le message « ***Merci et au revoir !*** »
            print("***Merci et au revoir !*** ")

    def alterner_tour(self, choix, j1, j2):
        """Cette methode permet d'alterner les tours entre les deux joueurs jusqu'à le plateau devient plein
         ou l'un de joueur gagne
          Args:
            choix: le mode du jeu (jeu entre deux personnes ou une personne et l'ordinateur
            j1 (joueur): le joueur qui prend le premier tour .
            j2 (joueur): le joueur qui prend le deuxiéme tourr.

        """
        assert isinstance(choix, int), "Partie: choix doit être un entier."
        assert choix in [1, 2], "Partie: choix doit être 1 ou 2."
        assert isinstance(j1, Joueur), "Partie: j1 doit être un Joueur."
        assert isinstance(j2, Joueur), "Partie: j2 doit être un Joueur."

        # On alterne entre le premier joueur et le deuxième joueur à chaque appel de tour()
        # Le jeu continue jusqu'à le plateu devient plein ou l'un de joueur gagne
        while self.plateau.non_plein() and not self.plateau.est_gagnant('X') and not self.plateau.est_gagnant("O"):
            # le plateau n'est pas encore plein et auncun n'a gagné
            # le tour du 1ér joueur
            self.joueur_courant = j1
            self.tour(choix)

            if self.plateau.non_plein() and not self.plateau.est_gagnant('X') and not self.plateau.est_gagnant("O"):
                # le plateau n'est pas encore plein et auncun n'a gagné
                # le tour du 2émé joueur
                self.joueur_courant = j2
                self.tour(choix)
                # si le plateau n'est pas encore plein et auncun n'a gagné on revient au 1ér joueur
                # sinon la partie est finie et les 2 joueurs n'ont pas encore du tours à jouer

    def partie_terminée(self, j1, j2):
        """La partie est terminée si le plateau est plein ou on a un gagnant,
         on affiche alors le joueur gagnant (s'il existe) et les statistiques sur le jeu.
         Args:
            choix: le mode du jeu (jeu entre deux personnes ou une personne et l'ordinateur
            self:
            j1 (joueur): le joueur qui prend le premier tour .
            j2 (joueur): le joueur qui prend le deuxiéme tourr.

        """
        assert isinstance(j1, Joueur), "Partie: j1 doit être un Joueur."
        assert isinstance(j2, Joueur), "Partie: j2 doit être un Joueur."
        if self.plateau.est_gagnant(j1.pion):
            j1.nb_parties_gagnees = j1.nb_parties_gagnees + 1
            print("Partie terminée! Le joueur gagnant est : ", j1.nom, "\n",
                  "Parties gagnées par ", j1.nom, " : ", j1.nb_parties_gagnees, "\n",
                  "Parties gagnées par ", j2.nom, " : ", j2.nb_parties_gagnees, "\n",
                  "Parties nulles: ", self.nb_parties_nulles, "\n", )

        elif self.plateau.est_gagnant(j2.pion):
            j2.nb_parties_gagnees = j2.nb_parties_gagnees + 1
            print("Partie terminée! Le joueur gagnant est:", j2.nom, "\n",
                  "Parties gagnées par ", j1.nom, " : ", j1.nb_parties_gagnees, "\n",
                  "Parties gagnées par ", j2.nom, " : ", j2.nb_parties_gagnees, "\n",
                  "Parties nulles: ", self.nb_parties_nulles, "\n", )
        else:
            self.nb_parties_nulles = 1 + self.nb_parties_nulles
            print("Partie terminée! Aucun joueur n'a gagné \n ",
                  "Parties gagnées par ", j1.nom, " : ", j1.nb_parties_gagnees, "\n",
                  "Parties gagnées par ", j2.nom, " : ", j2.nb_parties_gagnees, "\n",
                  "Parties nulles: ", self.nb_parties_nulles, "\n", )

    def saisir_nombre(self, nb_min, nb_max):
        """
        Permet de demander à l'utilisateur un nombre et doit le valider.
        Ce nombre doit être une valeur entre nb_min et nb_max.
        Vous devez utiliser la méthode isnumeric() afin de vous assurer que l'utilisateur entre
        une valeur numérique et non pas une chaîne de caractères.
        Veuillez consulter l'exemple d'exécution du jeu mentionné dans l'énoncé du TP
        afin de savoir quoi afficher à l'utilisateur.

        Args:
            nb_min (int): Un entier représentant le minimum du nombre à entrer.
            nb_max (int): Un entier représentant le maximum du nombre à entrer.

        Returns:
            int: Le nombre saisi par l'utilisateur après validation.
        """
        assert isinstance(nb_min, int), "Partie: nb_min doit être un entier."
        assert isinstance(nb_max, int), "Partie: nb_max doit être un entier."

        # pass
        # mon travail
        nb = input("Entrez s.v.p. un nombre entre 0 et 2 :? ")
        while not nb.isnumeric() or (int(nb) > nb_max) or (int(nb) < nb_min):
            print("***valeur incorrecte!***")
            nb = input("Entrez s.v.p. un nombre entre 0 et 2 :? ")
        return int(nb)

    def demander_forme_pion(self):
        """
        Permet de demander à l'utilisateur un caractère et doit le valider.
        Ce caractère doit être soit 'O' soit 'X'.
        Veuillez consulter l'exemple d'exécution du jeu mentionné dans l'énoncé du TP
        afin de savoir quoi afficher à l'utilisateur.

        Returns:
            string: Le catactère saisi par l'utilisateur après validation.
        """
        # pass
        # mon travail
        p = input("Selectionner s.v.p. la forme de votre pion: ?")
        while p != "X" and p != "O":
            p = input("Ressayer : Selectionner s.v.p. la forme de votre pion: ?")
        return p

    def tour(self, choix):
        """
        Permet d'exécuter le tour d'un joueur (une personne ou un ordinateur).
        Cette méthode doit afficher le plateau (voir la méthode __str__() de la classe Plateau).
        Si le joueur courant est un ordinateur, il faut calculer la position de la prochaine
        case à jouer par cet ordinateur en utilisant la méthode choisir_prochaine_case().
        Si le joueur courant est une personne, il faut lui demander la position de la prochaine
        case qu'il veut jouer en utilisant la méthode demander_postion().
        Finalement, il faut utiliser la méthode selectionner_case() pour modifier le contenu
        de la case choisie soit par l'ordinateur soit par la personne.

        Args:
            choix (int): Un entier représentant le choix de l'utilisateur dans le menu du jeu (1 ou 2).
        """

        assert isinstance(choix, int), "Partie: choix doit être un entier."
        assert choix in [1, 2], "Partie: choix doit être 1 ou 2."

        # pass
        # mon travail

        # Si le jeu est entre un utilisateur et l'ordinateur
        if choix == 1:
            # Si le joueur courant est un ordinateur,on calcule la position de la prochaine case
            if self.joueur_courant.type == "Ordinateur":
                print("C'est le tour maintenat de l'ordinateur Colosse")
                a, b = self.plateau.choisir_prochaine_case(self.joueur_courant.pion)
                self.plateau.selectionner_case(a, b, self.joueur_courant.pion)
                # afficher le plateau
                print(self.plateau.__str__())
            else:
                # Si le joueur courant est une personne,on lui demande la position de la prochaine case
                a, b = self.demander_postion()
                self.plateau.selectionner_case(a, b, self.joueur_courant.pion)
                # afficher le plateau
                print(self.plateau.__str__())
        else:
            # Si le jeu est entre 2 utilisateurs
            a, b = self.demander_postion()
            self.plateau.selectionner_case(a, b, self.joueur_courant.pion)
            print(self.plateau.__str__())

    def demander_postion(self):
        """
        Permet de demander à l'utilisateur les coordonnées de la case qu'il veut jouer.
        Cette méthode doit valider ces coordonnées (ligne,colonne).
        Voici un exemple de ce qu'il faut afficher afin de demander cette position:

        Mondher : Entrez s.v.p. les coordonnées de la case à utiliser:
        Numéro de la ligne:Entrez s.v.p. un nombre entre 0 et 2:? 0
        Numéro de la colonne:Entrez s.v.p. un nombre entre 0 et 2:? 0

        Il faut utiliser la méthode saisir_nombre() et position_valide().

        Returns:
            (int,int):  Une paire d'entiers représentant les
                        coordonnées (ligne, colonne) de la case choisie.
        """
        # pass
        # mon travail

        # Ici joueur_courant=none à l'initiation il faut faire appel à tour avant d'executer cette methode
        # On saisie le num de la ligne (compris entre 0 et 2)
        print(self.joueur_courant.nom + " : Entrez s.v.p. les coordonnées de la case à utiliser:")
        print("Numéro de la ligne:", end='')
        ligne = self.saisir_nombre(0, 2)

        # On saisie le num de la colonne (compris entre 0 et 2)
        print("Numéro de la colonne:", end='')
        colonne = self.saisir_nombre(0, 2)

        # On vérifie si les coordonnées entrés sont valides sinon on lui demande de refaire le remplissage
        while not self.plateau.position_valide(ligne, colonne):
            print("***la case est déjà occupée***")
            print("Numéro de la ligne:", end='')
            ligne = self.saisir_nombre(0, 2)

            # On saisie le num de la colonne (compris entre 0 et 2)
            print("Numéro de la colonne:", end='')
            colonne = self.saisir_nombre(0, 2)
        return ligne, colonne


if __name__ == "__main__":
    # Point d'entrée du programme.
    # On initialise une nouvelle partie, et on appelle la méthode jouer().
    partie1 = Partie()
    partie1.jouer()
