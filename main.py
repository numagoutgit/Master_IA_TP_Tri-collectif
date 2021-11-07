import numpy as np
import matplotlib.pyplot as plt

from environnement import *

#Choix des paramètres du tri
M = 50
N = 50
nA = 100
nB = 100
nAgent = 50
kplus = 0.1
kmoins = 0.3
t = 50
taux_erreur = 0
nbTour = 5000

#Choix des paramètres d'animation
animation_speed = 0.001
animation_freq = 100

jeu = Environnement(M,N,nA,nB,nAgent,kplus,kmoins,t,taux_erreur)

fig, ax = plt.subplots()

#Plot du début
(XA, YA) = jeu.coord_objet('A')
(XB, YB) = jeu.coord_objet('B')
(Xagent, Yagent) = jeu.coord_agents()
plot = ax.plot(XA, YA, 'bo', XB, YB, 'ro', Xagent, Yagent, 'k1')

#Permet d'actualiser le graphique
plt.pause(animation_speed)

jeu.run(nbTour, plot, fig, animation_speed, animation_freq)

#Plot de fin
(XA, YA) = jeu.coord_objet('A')
(XB, YB) = jeu.coord_objet('B')
(Xagent, Yagent) = jeu.coord_agents()
plot[0].set_data(XA,YA)
plot[1].set_data(XB,YB)
plot[2].set_data(Xagent,Yagent)

plt.show()