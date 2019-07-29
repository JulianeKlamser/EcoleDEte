import random
import math
from matplotlib import pyplot as plt
from matplotlib import animation

L = 5.0 # Longueur de la boite
N = 2 # Nombre de particules
dt = 0.01 # pas de temps discrets
print "\n****\nNous allons faire notre premiere animation maintenant ! Deux particules (N =", N, ") dans un carre de longueur d'arete L = ", L , "se deplaceront a une vitesse constante. Nous choisissons des positions initiales aleatoires. Nous choisissons des positions initiales aleatoires et des orientations aleatoires de la direction du mouvement (de la vitesse).\n\nPour faire une simulation, nous devons deplacer les particules un tout petit peu, puis prendre une photo, puis deplacer un tout petit peu a nouveau, prendre une photo, puis deplacer un tout petit peu, puis... Nous disons, nous discreditons le temps. Dans un petit intervalle de temps dt = ", dt, ", une particule se deplace sur une distance dx = dt * v (si elle a une vitesse constante v).\n\nVotre tache consiste a modifier les lignes 31 et 32, de sorte que les deux particules se deplacent dans des conditions limites periodiques. L'operateur modulo vous sera utile ici !\nComparez avec la solution de Code07aSolution.py\nAppelez ensuite Juliane pour apprendre comment transformer ces particules en oiseaux."

mot = raw_input("\nTappez ENTER pour continuer :\n")

XPos = [ random.uniform( 0.0, L) for i in range( N ) ] # Coordonnees x de la position des particules
YPos = [ random.uniform( 0.0, L) for i in range( N ) ] # Coordonnees y de la position des particules
Angle = [ random.uniform( 0.0, 2. * math.pi ) for i in range( N ) ] # angle d'orientation (Direction of movement)
ParticleOrder = [ i for i in range(N) ] # cree un tableau [0 1 2 3 ... N]

fig = plt.figure(figsize=(10, 10))
ax = plt.axes(xlim=( 0, L ), ylim=( 0, L ))
line, = ax.plot( [], [], 'ro', markeredgecolor = 'k', ms=10 )

def init(): #                   veuillez ignorer ceci
    line.set_data([], []) #     veuillez ignorer ceci
    return line, #              veuillez ignorer ceci

def animate( i ):
    random.shuffle( ParticleOrder ) # reorganise l'ordre des nombres dans le tableau de facon aleatoire
    for pA in ParticleOrder: # la boucle passe par toutes les entrees du tableau
        xVel = math.cos( Angle[ pA ] ) # Vitesse dans la direction x
        yVel = math.sin( Angle[ pA ] ) # Vitesse dans la direction y
        # Notez que sart( xVel**2 + yVel**2 ) = 1. Les particules ont une vitesse constante (v = 1).

        XPos[ pA ] = ( XPos[ pA ] + dt * xVel ) # changez ici
        YPos[ pA ] = ( YPos[ pA ] + dt * yVel ) # changez ici

    line.set_data(XPos, YPos)
    return line,

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=20, blit=False)

plt.show()
