# Game.py


################################################################################
#                                                                              #
#                      Classe "Game" pour le jeu PACMAN                        #
#                                                                              # 
################################################################################

# Ce fichier contient une classe mère "Game" dans laquelle le jeu se fait
# et où sont instantiées les différentes classes du jeu : Pacman, Playfield, Candy.
# La méthode “new_game()” définit le début de la partie.
# La méthode “end_of_game()” définit la fin de la partie.
# La méthode "tour()" gère le tour du jeu.

import Playfield
import Pacman 
import Candy
     
class Game: 
    """
    La classe Game prépare et initialise le jeu.
    ...
        
    Attributs
    ----------
    gamestate : bool
        Indique l'état du jeu (false le jeu n'est pas en cours, true le jeu est en cours).
   
    Methodes
    -------
    new_game :
        Lance le jeu et instancie les éléments nécessaires.
    tour :
        Définit les conditions de chaque tour de la partie.
    end_of_game :
        Vérifie si Nicepacman ou Badpacman est mort, ou si Nicepacman a rempli sa jauge à 100 et si tel est le cas met fin à la partie.
    
    """
    def __init__(self, gamestate):
        
        """
        Initialise l'état du jeu et instancie les classes pacman (Nice et Bad), Playfield et Candy. On définit ici également une liste des candies. 
        
        Attributes
        ----------
        gamestate : bool
            Renseigne sur l'état de la partie (false, la partie n'est pas en cours, true la partie est en cours).
        
        """
        self.nicepacman1 = Pacman.NicePacman([7,7],True, 0)
        self.badpacman1 = Pacman.BadPacman([8,7],True, 100)
        self.terrain = Playfield.Playfield()
        self.candy1 = Candy.Candy([8,8],10,True)
        self.candy2 = Candy.Candy([7,8],10,True)
        self.candy3 = Candy.Candy([3,8],10,True)
        self.candy4 = Candy.Candy([5,6],10,True)
        self.candy5 = Candy.Candy([2,5],5,True)
        self.list_candies=[self.candy1, self.candy2, self.candy3, self.candy4, self.candy5]
        self.gamestate = gamestate
    
    def new_game(self):
        """
        Lance le jeu en instanciant la matice et en affichage les paramètres des deux pacman.      
     
        """
        print("---------------------------------")
        start=str(input("👾 Tape Go pour commencer 👾 \n > "))
        if start=="Go":
            print("Allez c'est parti ! 🕹 ")
            print("---------------------------------")
            self.terrain.create_matrice()
            self.nicepacman1.show_parameters()
            self.badpacman1.show_parameters()
            
    def tour (self, jeu): #J'ai un doute sur celui là
        """
        Définit les conditions de chaque tour de la partie en appelant les méthodes successivement pour chaque Pacman.
        1) move() pour déplacer le pacman
        2) is_wall() pour tester si on rencontre un mur ou pas
        3) eat() si un bonbon est rencontré
        4) enf_of_game() vérifie une des trois condition de victoire est atteinte ou non. 

        Nicepacman joue avant Badpacman.

        Attributs
        ----------
        jeu : objet
            Correspond à la partie en cours.
        
        """       
        print("---------------------------------")
        print ("🟡 Déplacement Nicepacman 🟡 ")
        self.nicepacman1.move()
        if self.terrain.is_wall(self.nicepacman1.position) == True:
            print("Oups Nice 🟡, c'est un mur, tu dois de déplacer à nouveau !")
            self.nicepacman1.move()
        else:
            for candy in self.list_candies:
                if self.nicepacman1.position == candy.position:
                    self.nicepacman1.eat(candy, self.nicepacman1)
        self.nicepacman1.is_dead(self.badpacman1)
        jeu.end_of_game()


        if (self.nicepacman1.pacmanstate) == True and self.gamestate == True :
            print("---------------------------------")
            print ("🔴 Déplacement Badpacman 🔴")
            self.badpacman1.move()
            if self.terrain.is_wall(self.badpacman1.position) == True:
                print("Oups Bad 🔴, c'est un mur, tu dois de déplacer à nouveau !")
                self.badpacman1.move()
            else:
                for candy in self.list_candies:
                    if self.badpacman1.position == candy.position and candy.status==True :
                        self.badpacman1.eat(candy, self.badpacman1)
            self.badpacman1.is_dead(self.nicepacman1)
            jeu.end_of_game()
                    
    def end_of_game(self):
            """
            Définit les conditions de fin de partie et de victoire.
            
            Retours
            -------
            gamestate : bool
                Indique si oui ou non l'une des conditions de victoire est atteinte ou non. 
                Pacman mort (Nice en se faisant manger, Bad ayant sa jauge à Zéro)
                ou Nicepacman avec sa jauge à 100.

            """
            if self.nicepacman1.jauge >= 100:
                print("Bravo 🎉🎉🎉 ! Tu as gagné ta jauge est à 100, Le méchant a perdu !")
                self.gamestate = False
                return self.gamestate
            elif (self.nicepacman1.pacmanstate == False) or (self.badpacman1.pacmanstate == False) :
                self.gamestate = False
                return self.gamestate
            else:
                self.gamestate = True
                return self.gamestate