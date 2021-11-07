import numpy as np

class Agent:
    """Agent dans le tableau. Peut se déplacer dans le tableau, ramasser/déposer un objet avec une probabilité. Possède une mémoire d'un nombre des cells visitées précédemment.
       Attribut :
         - kplus : Constante de probabilite de prise
         - kmoins : Constante de probabilite de dépot
         - memoire : Liste de taille t représentant la mémoire de l'agent
         - taux_erreur : Taux d'erreur de dicernement des objets"""

    def __init__(self, kplus, kmoins, t, taux_erreur):
        self.kplus = kplus
        self.kmoins = kmoins
        self.memoire = ['O' for i in range(t)]
        self.taux_erreur = taux_erreur