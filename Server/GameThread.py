#! /bin/ipython3

from Game import *
from threading import Thread

class GameThread(Thread):

    #initialisation du serveur
    def __init__(self, gamesize = 10000, nbSpherePnj=100, nbMaxSpherePnj=10, minTailleSpheresPnj=1, maxTailleSpheresPnj=3):
        """
        gamesize                Taille du jeu en unités metriques (la carte est carrée)
        nbSpherePnj             nombre de spheres qu'a le PNJ au début
        nbMaxSpherePnj          nombre maximum de spheres qu'a le PNJ
        minTailleSpheresPnj     taille minimum d'une Sphere du PNJ
        maxTailleSpheresPnj     taille maximum d'une Sphere du PNJ
        """
        Thread.__init__(self)
        self.game = Game(gamesize, nbSpherePnj, nbMaxSpherePnj, minTailleSpheresPnj, maxTailleSpheresPnj)
        self.data = self.game.toJson()

    #boucle du jeu
    def run(self):
        while True:
            #si il y a un nouveau joueur
            pass