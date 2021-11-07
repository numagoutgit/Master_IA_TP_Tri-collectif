import numpy as np

from cell import *
from objet import *
from agents import *

class Environnement:
    """Tableau de MxN cell où sont disposé des agents et des objets.
       Attributes :
         - M : Nombre de ligne du tableau
         - N : Nombre de colonne du tableau
         - tableau : Matrice de MxN cell
         - nA : Nombre d'objet de type A
         - nB : Nombre d'objet de type B
         - nAgent : Nombre d'agent
         - kplus : Constante de probabilite de prise
         - kmoins : Constante de probabilite de dépot
         - t : Mémoire des agents
         - taux_erreur : Pourcentage d'erreur dans la reconnaissance d'objet"""

    def __init__(self, M, N, nA, nB, nAgent, kplus, kmoins, t, taux_erreur):
        self.M = M
        self.N = N
        self.kplus = kplus
        self.kmoins = kmoins
        self.t = t
        self.taux_erreur = taux_erreur

        self.init_tableau(M, N, nA, nB, nAgent)

    def init_tableau(self, M, N, nA, nB, nAgent):
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
               
        #Placement aléatoire des agents
        for k in range(nAgent):
            x = np.random.randint(M)
            y = np.random.randint(N)
            while self.tableau[x,y].agent != None:
                x = np.random.randint(M)
                y = np.random.randint(N)
            self.tableau[x,y].set_agent(Agent(self, self.tableau[x, y], self.kplus, self.kmoins, self.t, self.taux_erreur))

    def __str__(self):
        str = ""
        for i in range(self.M):
            ligne = "["
            for j in range(self.N):
                ligne+=self.tableau[i,j].toString()+"; "
            ligne = ligne[:-2] + "]"
            str += ligne +"\n"
        return str

jeu = Environnement(5,5,8,8,15,1,1,1,1)
print(jeu)