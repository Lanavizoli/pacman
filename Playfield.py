# Playfield.py


################################################################################
#                                                                              #
#                      Classe "Playfield" pour le jeu PACMAN                   #
#                                                                              # 
################################################################################

# Ce fichier contient une classe "Playfield" qui définit la forme du terrain.
# La méthode "create_matrice()" permet de créer le terrain de jeu et est utilisée
# par la classe "game" pour instancier la matrice.
# La méthode "is_wall()" permet de renvoyer la valeur booléenne d'un point de la matrice.

import numpy as np

class Playfield():
    """
    Classe implémentant le terrain de jeu.
    
    ...

    Methodes
    -------
    create_matrice:
        Permet de créer la matrice booléenne du terrain de jeu par un array en 2 dimensions (9 lignes * 9 colonnes)
    
    is_wall:
        Annonce au Pacman qu'il ne peut pas se déplacer sur les "True" ou "1" 
        de la matrice puisque définis comme des murs.
       

    """

    def __init__(self):
        """
        Initialise le terrain de jeu
        """
        self.create_matrice()

    def create_matrice(self):
        """
        Permet de créer la matrice du terrain de jeu avec un array en 2 dimensions.
        """
            # 0, 1, 2, 3, 4, 5, 6, 7, 8
            #ligne puis colonne
        self.matrice = np.array([
            [0, 0, 0, 0, 0, 0, 0, 0, 0],  # 0
            [0, 1, 1, 1, 1, 0, 1, 0, 0],  # 1
            [0, 1, 0, 0, 1, 0, 1, 0, 0],  # 2
            [0, 0, 0, 0, 0, 0, 1, 0, 0],  # 3
            [0, 1, 0, 0, 1, 1, 1, 1, 0],  # 4
            [0, 1, 0, 0, 0, 0, 0, 0, 0],  # 5
            [0, 1, 0, 1, 0, 0, 1, 0, 0],  # 6
            [0, 1, 1, 1, 0, 1, 1, 0, 0],  # 7
            [0, 0, 0, 0, 0, 0, 1, 0, 0]   # 8
        ], dtype=bool)
        print("---------------------------------")
        print("Voici le terrain de jeu \n Tu peux te déplacer sur les True, les False sont des murs \n \n")
        print(self.matrice)
        
    def is_wall(self, positionpacman): 
        """
        Vérifie et averti le joueur s'il rencontre ou non un mur 
        ==> il nous manque les lignes pour rendre impossible de se placer sur une case "mur" (True) pour un pacman
        ==> On a juste le message pour l'instant

        Paramètres
        ----------
        positionpacman : array int
            Correspond aux coordonnées matricielles du pacman joué.
            0 étant la première valeur de la position.
            1 étant la deuxième valeurs.

        Retours
        -------
        bool            
            Indique si oui ou non le joueur rencontre un mur.         
            Retourne un True s'il y a un mur (défini comme 1 dans la matrice).
            Retourne un False s'il n'y a pas de mur (défini comme 0 dans la matrice).
        """
        return self.matrice[positionpacman[0]][positionpacman[1]]

#---------------------------------
#Pf = Playfield()
#matrice = Pf.create_matrice()