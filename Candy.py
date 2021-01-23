# Candy.py


################################################################################
#                                                                              #
#                      Classe "Candy" pour le jeu PACMAN                       #
#                                                                              # 
################################################################################

# Ce fichier contient la classe "Candy".
# La méthode "meet_pacman()" retourne un booléen indiquant si 
# le candy est rencontré par un Pacman ou non
# Un candy a une puissance, une position et un statut.

import Pacman as pc 

class Candy():
    """
    Classe implémentant un bonbon.
    
    ...
    
    Attributs
    ----------
    position : int
        Indique la position des Candies sur la matrice
    power : int
        Renseigne sur la puissance des Candies (5 ou 10)
    status : bool
        Renseigne sur la visibilité des Candies sur la matrice

    Methodes
    -------
    meet_pacman :
        Permet d'indiquer si le candy est mangé par un Pacman
        Si tel est le cas, il n'appararaitra plus sur la matrice et son statut devient False
    """

    def __init__(self, position, power, status):
        """
        Initialise le Candy avec une position, un pouvoir et un statut

        ...

        Paramètres
        ----------
        position: int
            Renseigne sur la position dans la matrice, array
        power : int
            Renseigne sur la puissance du candy (5 ou 10)
        status : bool
            Indique si le candy est mangé par un Pacman (True si toujours présent, False si mangé)
        """
        self.position = position
        self.power = power
        self.status = status
    
    def meet_pacman (self, pacman):
        """
        Définit si un Candy est mangé ou non par un Pacman

        ...

        Paramètres
        ----------
        pacman : objet
            Correspond aux personnages joués instanciés, nicepacman ou badpacman

        Retours
        -------
        self.status : bool
            Indique si oui ou non le Candy est mangé
            avec status True le Candy est visible sur le jeu est n'est pas mangé
            et False si un Pacman et un Candy sont sur la même position, donc sera mangé 
            
        """      
        if pacman.position == self.position:
            self.status = False
            return True
        else:
            self.status = True

#--------------------------------
# Test
#candy1 = Candy([8,1],10,True)
#candy2 = Candy([6,3],10,True)
#np = Pacman.NicePacman([8,1],0)
#bp = Pacman.BadPacman([6,3],100)