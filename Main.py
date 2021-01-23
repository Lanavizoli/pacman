# Main.py

################################################################################
#                                                                              #
#                                  PACMAN                                      #
#                                                                              #
#               Adaptation libre du célèbre jeu japonais Pac Man               #
#                                                                              #
#                       langage : Python 3.8                                   # 
#                       date    : 22/01/2021                                   #
#                       version : 1.0                                          #
#                       auteurs  : L.Vinet, L.Vizeu Oliveira, H.Bonneville     #
#                                                                              # 
################################################################################

# Ce fichier constitue le fichier principal du programme qui appelle tous les autres.

import Game as gm 

jeu = gm.Game(True)

while jeu:
    jeu.new_game()
    while jeu.gamestate == True:
        jeu.tour(jeu)    
    else:
        print("---------------------------------")
        suite=input("🕹 Veux-tu recommencer? 🕹 oui ou non \n > ")
        if suite == 'non':
            print ("Byyyye 👋🏽")
            del jeu
        elif suite == 'oui':
            print ("C'est reparti ! 👾")
            jeu.gamestate = True
            del jeu
            jeu = gm.Game(True)