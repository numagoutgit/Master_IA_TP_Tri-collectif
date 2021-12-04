import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

from environnement import *

#Choix des paramètres du tri
M = 50
N = 50
nA = 100
nB = 100
nAgent = 50
kplus = 0.1
kmoins = 0.3
t = 10
taux_erreur = 0
nbTour = 5000

#Choix des paramètres d'animation
animation_speed = 0.001 #temps en seconde entre 2 images
animation_freq = 5 #Nombre de tour entre 2 images

jeu = Environnement(M,N,nA,nB,nAgent,kplus,kmoins,t,taux_erreur)

fig, ax = plt.subplots()

#On demande à l'utilisateur s'il veut sauvegarder l'animation
reponse_user = input("Voulez-vous sauvegarder l'animation (y/n, defaut n)? (Si y, le programme prendra plus de temps à démarrer, et pour un nbTour trop élevé avec un animation_freq trop faible, le programme risque de ne pas fini) ")
savefile = reponse_user == 'y'

#Plot du début
(XA, YA) = jeu.coord_objet('A')
(XB, YB) = jeu.coord_objet('B')
(Xagent, Yagent) = jeu.coord_agents()
plot = ax.plot(XA, YA, 'bo', XB, YB, 'ro', Xagent, Yagent, 'k1')
fig.suptitle('Taille mémoire = '+str(t)+"; Taux d'erreur = "+str(taux_erreur))


if not savefile:
    #Permet d'actualiser le graphique
    plt.pause(animation_speed)

    jeu.run_without_saving(nbTour, plot, fig, animation_speed, animation_freq)

    #Plot de fin
    (XA, YA) = jeu.coord_objet('A')
    (XB, YB) = jeu.coord_objet('B')
    (Xagent, Yagent) = jeu.coord_agents()
    plot[0].set_data(XA,YA)
    plot[1].set_data(XB,YB)
    plot[2].set_data(Xagent,Yagent)
else:
    XA, YA, XB, YB, Xagent, Yagent = jeu.run_with_saving(nbTour)

    def update(i):
        actual_i = i*animation_freq
        if actual_i < nbTour:
            plot[0].set_data(XA[actual_i], YA[actual_i])
            plot[1].set_data(XB[actual_i], YB[actual_i])
            plot[2].set_data(Xagent[actual_i], Yagent[actual_i])
        else:
            plot[0].set_data(XA[-1], YA[-1])
            plot[1].set_data(XB[-1], YB[-1])
            plot[2].set_data(Xagent[-1], Yagent[-1])

    animation = anim.FuncAnimation(fig, update, frames = nbTour//animation_freq +1 , interval = animation_speed*1000, repeat = False)

    #Saving animation
    f = r"animation.gif"
    writergif = anim.PillowWriter(fps=int(1/animation_speed))
    animation.save(f, writer=writergif)

plt.show()
