import numpy as np

from cell import *
from objet import *

class Agent:
    """Agent dans le tableau. Peut se déplacer dans le tableau, ramasser/déposer un objet avec une probabilité. Possède une mémoire d'un nombre des cells visitées précédemment.
       Attribut :
         - env : Environnement où prend place l'agent
         - cellule : Cellule où se situe l'agent
         - objet : L'objet qu'il est en train de porter (None si aucun)
         - kplus : Constante de probabilite de prise
         - kmoins : Constante de probabilite de dépot
         - memoire : Liste de taille t représentant la mémoire de l'agent
         - taux_erreur : Taux d'erreur de discernement des objets (valeur par defaut = 0)"""

    directions = [[1,0], [-1,0], [0,1], [0,-1], [1,1], [1,-1], [-1,1], [-1,-1]]

    def __init__(self, env, cellule, kplus, kmoins, t, taux_erreur=0):
        self.env = env
        self.cellule = cellule
        self.objet = None
        self.kplus = kplus
        self.kmoins = kmoins
        self.memoire = ['O' for i in range(t)]
        self.taux_erreur = taux_erreur

    def f(self, type):
      """Calcule la proportion d'objet dans la memoire"""
      nbA = 0
      nbB = 0
      for o in self.memoire:
        if o == 'A':
          nbA += 1
        elif o == 'B':
          nbB += 1
      if type == 'A':
        return (nbA + nbB*self.taux_erreur)/len(self.memoire)
      else:
        return (nbB + nbA*self.taux_erreur)/len(self.memoire)

    def proba_prise(self, type):
      """Probabilite de saisir l'objet de type"""
      return (self.kplus/(self.kplus + self.f(type)))**2

    def proba_depot(self, type):
      """Probabilite de deposer l'objet de type"""
      return (self.kmoins/(self.kmoins + self.f(type)))**2

    def perception(self):
      """Renvoie les cellules voisines de l'agent disponible"""
      x = self.cellule.x
      y = self.cellule.y
      voisin_disponible = []
      for dir in Agent.directions:
        new_x = x+dir[0]
        new_y = y+dir[1]
        if new_x>=0 and new_x<self.env.M and new_y>=0 and new_y<self.env.M:
          cellule = self.env.tableau[new_x, new_y]
          if cellule.agent == None:
            voisin_disponible.append(cellule)
      return voisin_disponible

    def actualiser_memoire(self, cellule_suivante):
      """Actualise la mémoire de l'agent"""
      if cellule_suivante.objet == None:
        type = 'O'
      else:
        type = cellule_suivante.objet.type
      self.memoire = [type] + self.memoire[:-1]

    def move(self,cellule_suivante):
      """Deplacement de l'agent vers la cellule"""
      self.cellule.set_agent(None)
      cellule_suivante.set_agent(self)
      self.cellule = cellule_suivante
      self.actualiser_memoire(cellule_suivante)

    def prendre_objet(self):
      """Prend l'objet situé sur sa cellule"""
      self.objet = self.cellule.objet
      self.cellule.set_objet(None)

    def depot_objet(self):
      """Dépose l'objet sur sa cellule"""
      self.cellule.set_objet(self.objet)
      self.objet = None

    def choix_deplacement(self):
      """Choisi son déplacement de manière aléatoire"""
      voisin = self.perception()
      return voisin[np.random.randint(len(voisin))]

    def action(self):
      """Enclenche l'action de l'agent"""
      new_cellule = self.choix_deplacement()
      self.move(new_cellule)
      if self.objet == None:
        if self.cellule.objet != None:
          proba = self.proba_prise(self.cellule.objet.type)
          if np.random.rand() < proba:
            self.prendre_objet()
      else:
        if self.cellule.objet == None:
          proba = self.proba_depot(self.cellule.objet.type)
          if np.random.rand() < proba:
            self.depot_objet(self.objet)