import numpy as np

from agents import *
from objet import *

class Cell:
    """Case du tableau; elle peut contenir un objet (A ou B), un agent ou les deux.
       Attribute :
         - agent : l'agent sur la cell ou None si aucun
         - objet : A, B ou None si aucun"""

    def __init__(self, agent, objet):
        self.agent = agent
        self.objet = objet

    def set_agent(self, agent):
        self.agent = agent

    def set_objet(self, objet):
        self.objet = objet

    def toString(self):
        if self.objet == None:
            obj = 'O'
        else:
            obj = self.objet.type
        if self.agent == None:
            ag = ' '
        else:
            ag = 'X'
        return ("("+obj+","+ag+")")