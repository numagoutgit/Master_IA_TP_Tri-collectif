import numpy as np
import matplotlib.pyplot as plt

from cell import *
from objet import *
from agents import *

class Environnement:
    """Tableau de MxN cell où sont disposé des agents et des objets.
       Attributes :
         - M : Nombre de ligne du tableau
         - N : Nombre de colonne du tableau
         - att_pheromone : taux d'atténuation des phéromones
         - tableau : Matrice de MxN cell"""

    def __init__(self, M, N, nA, nB, nC, nAgent, kplus, kmoins, t, S, att_pheromone, temps_attente):
        """Initialise l'environnement
           - nA : Nombre d'objet de type A
           - nB : Nombre d'objet de type B
           - nC : Nombre d'objet de type C
           - nAgent : Nombre d'agent
           - kplus : Constante de probabilite de prise
           - kmoins : Constante de probabilite de dépot
           - t : Mémoire des agents"""
        self.M = M
        self.N = N
        self.att_pheromone = att_pheromone

        self.init_tableau(M, N, nA, nB, nC, nAgent, kplus, kmoins, t, S, temps_attente)

    def init_tableau(self, M, N, nA, nB, nC, nAgent, kplus, kmoins, t, S, temps_attente):
        self.tableau = np.zeros((M,N),dtype=Cell)
        #Création des cellules vides
        for i in range(M):
            for j in range(N):
                self.tableau[i,j] = Cell(i, j, None, None)

        #Placement aléatoire des objets A
        for k in range(nA):
            x = np.random.randint(M)
            y = np.random.randint(N)
            while self.tableau[x,y].objet != None:
                x = np.random.randint(M)
                y = np.random.randint(N)
            self.tableau[x,y].set_objet(Objet('A'))
        
        #Placement aléatoire des objets B
        for k in range(nB):
            x = np.random.randint(M)
            y = np.random.randint(N)
            while self.tableau[x,y].objet != None:
                x = np.random.randint(M)
                y = np.random.randint(N)
            self.tableau[x,y].set_objet(Objet('B'))

        #Placement aléatoire des objets C
        for k in range(nC):
            x = np.random.randint(M)
            y = np.random.randint(N)
            while self.tableau[x,y].objet != None:
                x = np.random.randint(M)
                y = np.random.randint(N)
            self.tableau[x,y].set_objet(Objet('C'))
               
        #Placement aléatoire des agents
        for k in range(nAgent):
            x = np.random.randint(M)
            y = np.random.randint(N)
            while self.tableau[x,y].agent != None:
                x = np.random.randint(M)
                y = np.random.randint(N)
            self.tableau[x,y].set_agent(Agent(self, self.tableau[x, y], kplus, kmoins, t, S, temps_attente))

    def coord_agents(self):
        """Renvoie les coordonnées de tous les agents sur le terrain, cette fonction sert pour la représentation graphique"""
        X = []
        Y = []
        for i in range(self.M):
            for j in range(self.N):
                if self.tableau[i,j].agent != None:
                    X.append(i)
                    Y.append(j)
        return (X,Y)

    def coord_objet(self, type):
        """Renvoie les coordonnées de tous les objets de type, fonction à but graphique"""
        X = []
        Y = []
        for i in range(self.M):
            for j in range(self.N):
                if self.tableau[i,j].objet != None:
                    if self.tableau[i,j].objet.type == type:
                        X.append(i)
                        Y.append(j)
        return (X,Y)

    def run_without_saving(self, n, plots, fig, animation_speed, animation_freq):
        """Fonction qui lance la simulation et actualise le graphique"""
        for k in range(n):
            for i in range(self.M):
                for j in range(self.N):
                    if self.tableau[i,j].agent != None:
                        self.tableau[i,j].agent.action()
                        self.tableau[i,j].attenuation_pheromone(self.att_pheromone)

            #Actualise le graphique a une fréquence donnée et un vitesse donnée
            if k%animation_freq == 0:
                (X,Y) = self.coord_objet('A')
                plots[0].set_data(X,Y)

                (X,Y) = self.coord_objet('B')
                plots[1].set_data(X,Y)

                (X,Y) = self.coord_objet('C')
                plots[2].set_data(X,Y)

                (X,Y) = self.coord_agents()
                plots[3].set_data(X,Y)

                #Permet d'actualiser le graphique
                plt.pause(animation_speed)

    def run_with_saving(self, n):
        """Fonction qui lance la simulation et renvoie toutes les données à animer"""
        XA = []
        YA = []
        XB = []
        YB = []
        XC = []
        YC = []
        Xagent = []
        Yagent = []
        for k in range(n):
            for i in range(self.M):
                for j in range(self.N):
                    if self.tableau[i,j].agent != None:
                        self.tableau[i,j].agent.action()
                        self.tableau[i,j].attenuation_pheromone(self.att_pheromone)

            (X,Y) = self.coord_agents()
            Xagent.append(X)
            Yagent.append(Y)
            (X,Y) = self.coord_objet('A')
            XA.append(X)
            YA.append(Y)
            (X,Y) = self.coord_objet('B')
            XB.append(X)
            YB.append(Y)
            (X,Y) = self.coord_objet('C')
            XC.append(X)
            YC.append(Y)
        return(XA, YA, XB, YB, XC, YC, Xagent, Yagent)