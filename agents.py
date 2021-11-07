import numpy as np

class Agent:
    """Agent dans le tableau. Peut se déplacer dans le tableau, ramasser/déposer un objet avec une probabilité. Possède une mémoire d'un nombre des cells visitées précédemment.
       Attribut :
         - kplus : Constante de probabilite de prise
         - kmoins : Constante de probabilite de dépot
         - memoire : Liste de taille t représentant la mémoire de l'agent
         - taux_erreur : Taux d'erreur de discernement des objets (valeur par defaut = 0)"""

    def __init__(self, kplus, kmoins, t, taux_erreur=0):
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