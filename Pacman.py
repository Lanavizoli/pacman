# Pacman.py


################################################################################
#                                                                              #
#                      Classe "Pacman" pour le jeu PACMAN                      #
#                                                                              #
################################################################################


# Ce fichier contient la classe mère "Pacman" qui créer un personnage contrôlable
# par le joueur.
# Un Pacman a une position de départ et un statut.
# La méthode "move()" définit le déplacement des Pacmans
# Les sous-classes "NicePacman" et "BadPacman" héritent de leur classe mère.
# Tous deux ont une jauge différente lors de l'instantiation.
# La méthode "eat()" définit les conditions pour manger un bonbon pour chaque personnage.
# La méthode "is_dead()" définit les conditions de mort pour chaque personnage.
# La méthode "show_parameters()" affiche les paramètres relatifs à chaque personnage.

class Pacman():
    """
    Classe pour Pacman

    ...
    
    Attribus
    ----------
    position : list (x;y)
        Renseigne les coordonnées matricielles du pacman sur le terrain de jeu
    pacmanstate : bool
        Indique l'état du pacman au cours de la partie (mort = False, Vivan = True)
    
    Methodes
    -------
    move :
        Initie le déplacement du pacman joué en renvoie sa nouvelle position
    """    

    def __init__(self, position, pacmanstate):
        """
        Initialise les caractéristiques du pacman joué avec une jauge et une position

        Parameters
        ----------
        position : list (x;y)
            Renseigne les coordonnées matricielles du pacman sur le terrain de jeu
        pacmanstate : bool
            Indique l'état du pacman au cours de la partie (mort = False, Vivan = True)

        """
        self.position = position      
        self.pacmanstate = pacmanstate
        
    def move(self):
        """
        Initie le déplacement du pacman joué et renvoie sa nouvelle position
        Affiche la nouvelle position du joueur sur le terrain

        """
        moving = input("Pour te déplacer, appuie sur Q pour aller à gauche, D pour la droite, Z en haut, S en bas \n > ")
        if moving == "s":
            self.position[0] += 1
        elif moving == "z":
            self.position[0] -= 1
        elif moving == "q":
            self.position[1] -= 1
        elif moving == "d":
            self.position[1] += 1
        print (self.position)


######################################################################
#                      sous-classe "NicePacman"                      #
######################################################################

class NicePacman(Pacman):
    """
    Sous-classe pour le joueur incarnant le Pacman "NicePacman"
    Modifie le nombre de points de jauge au départ de la partie,
    la manière de perdre le jeu et les conséquences de l'action de manger un bonbon.
    
    Pour le NicePacman :
    Jauge de départ : 0 point
    Manger un bonbon : jauge + 5 ou + 10 points
    Etre mangé par l'autre joueur BadPacman : perte de la partie

    ...
    
    Attribus
    ----------
    position : list
        Renseigne les coordonnées matricielles du pacman sur le terrain de jeu
    pacmanstate : bool
        Indique l'état du pacman au cours de la partie
    jaugepleine : bool
        Indique si oui ou non la jauge du pacman joué est pleine
    jauge : int
        Renseigne le nombre (entier) de points score du pacman joué
    
    Méthodes
    -------
    eat :
        Initialise l'action de manger du pacman joué.
        Ajoute un certain nombre de points relatif
        à la puissance du bonbon mangé à la jauge du joueur.
        
    is_dead :
        Conclue sur la mort ou non du pacman joué.
        
    show_parameters :
        Affiche les caractéristiques du pacman joué (jauge, position).

    """   

    def __init__(self, position, pacmanstate, jauge=0):
        """
        Initialise les caractéristiques du nicepacman joué.

        Paramètres
        ----------
        position : list
            Renseigne les coordonnées matricielles du pacman sur le terrain de jeu.
        pacmanstate : bool
            Indique l'état du pacman au cours de la partie.
        jauge : int
            Initialise à 0 le nombre de points score du pacman joué.

        """
        Pacman.__init__(self, position, pacmanstate)
        self.jauge = jauge
        self.jaugepleine = False

    def eat (self, bonbon, nicepacman):
        """
        Initialise l'action de manger du nicepacman joué.
        Ajoute un certain nombre de points (5 ou 10) relatif
        à la puissance du bonbon mangé à la jauge du joueur.
        
        Parameters
        ----------
        bonbon : objet
            Correspond à un candy sur le terrain.
        nicepacman : objet
            Correspond au personnage NicePacman instancié donné à la méthode meet, appelée dans la méthode eat.
        
        """             
        if bonbon.meet_pacman(nicepacman) == True :
            self.jauge += bonbon.power
            print ('🍒🧁 Yummy ! 🍒🧁')
        print ("Nice 🟡, ta jauge est à : ", self.jauge)
        
    def is_dead(self, badpacman):
        """
        Conclue sur la mort du NicePacman joué. Lorsqu'il atteint la même
        position que l'autre joueur BadPacman, le joueur NicePacman meurt et
        perd la partie.
        
        Parameters
        ----------
        badpacman : objet
            Correspond au personnage BadPacman instancié. 
        
        Retourne
        -------
        pacman state : bool
            Indique si oui ou non le NicePacman joué est mort.

        """
        
        if badpacman.position == self.position:
            print("Oupsi, tu as perdu 😭 ! Tu t'es fait mangé par le méchant!")
            self.pacmanstate = False 
            return self.pacmanstate
        else:
            print(self.jauge)

    def show_parameters(self):
        
        """
        Affiche les caractéristiques du nicepacman joué (jauge, position).

        """
        print ("Paramètres Nice 🟡 : \n >")
        print(self.jauge)
        print(self.position)


######################################################################
#                      sous-classe "BadPacman"                      #
######################################################################

class BadPacman(Pacman):
    """
    Sous-classe pour le joueur incarnant le Pacman "BadPacman".
    Modifie le nombre de points de jauge au départ de la partie,
    la manière de perdre le jeu et les conséquences de l'action de manger un bonbon.
    
    Pour le BadPacman :
    Jauge de départ : 100 points
    Manger un bonbon : jauge - 5 ou - 10 points
    Jauge à 0 point : perte de la partie

    ...
    
    Attribus
    ----------
    position : list
        Renseigne les coordonnées matricielles du pacman joué sur le terrain de jeu
    pacmanstate : bool
        Indique l'état du pacman au cours de la partie
    jauge : int
        Renseigne le nombre (entier) de points score du pacman joué
        
    Méthodes
    -------
    eat :
        Initialise l'action de manger du pacman joué.
        Retire un certain nombre de points relatifs
        à la puissance du bonbon mangé à la jauge du joueur.
        
    is_dead :
        Conclue sur la mort du pacman joué.
        
    show_parameters :
        Affiche les caractéristiques du pacman joué (jauge, position).

    """ 
    
    def __init__(self, position, pacmanstate, jauge=100): 
        """
        Initialise les caractéristiques du pacman joué.

        Parameters
        ----------
        position : list
            Renseigne les coordonnées matricielles du pacman sur le terrain de jeu.
        pacmanstate : bool
            Indique l'état du pacman au cours de la partie.
        jauge : int
            Initialise à 100 le nombre de points score du pacman joué.

        """
        Pacman.__init__(self, position, pacmanstate)
        self.jauge = jauge

    def eat(self, bonbon, badpacman):
   
        """
        Initialise l'action de manger du pacman joué.
        Retire un certain nombre de points (5 ou 10) relatif
        à la puissance du bonbon mangé à la jauge du joueur.
        
        Paramètres
        ----------
        bonbon : objet
            Correspond à un candy instancié.
        badpacman : objet
            Correspond au personnage BadPacman instancié dont la méthode meet, appelée dans cette méthode eat a besoin.
        
        """         
        if bonbon.meet_pacman(badpacman) == True:
            self.jauge -= bonbon.power
            print ('🍒🧁 Aïe aïe aïe! 🍒🧁')
        print ("Bad 🔴, ta jauge est à : ", self.jauge)

    def is_dead(self, nicepacman):
        """
        Conclue sur la mort du BadPacman joué. Lorsqu'il atteint une jauge
        de 0 point, le BadPacman meurt et perd la partie.

        Paramètres
        ----------
        nicepacman : objet
            Correspond au personnage NicePacman.
        
        Retours
        -------
        pacmanstate : bool
            Indique si oui ou non le BadPacman joué est mort.

        """
        if self.jauge == 0:
            print("Oupsi, tu as perdu 😭 ! Tu n'as plus de point !")
            self.pacmanstate = False
            return self.pacmanstate
        else:
            print(self.jauge)             

    def show_parameters(self):
        """
        Affiche les caractéristiques du badpacman joué (jauge, position).

        """
        print ("Paramètres Bad 🔴 : \n >")
        print(self.jauge)
        print(self.position)

#-----------------------------------------------------------------------------
# Test
#np = NicePacman([4,7])
#bp = BadPacman([2,1])

#np.show_parameters()
#bp.show_parameters()