import sys
import matplotlib.pyplot as plt
import random

L = 5.0 # Longueur de la boite
N = 3 # Nombre de particules
print "\n****\nL =", L, "et N =", N

# positions x et y aleatoires des particules dans l'intervalle 0...L
X = [ random.uniform( 0.0 , L ) for i in range(N) ]
Y = [ random.uniform( 0.0 , L ) for i in range(N) ]
print "positions x aleatoires = ", X
print "positions y aleatoires = ", Y

print "\nExercise : Ouvrez le code et essayez de comprendre comment les particules sont dessinees. N'hesitez pas a modifier les parametres (comme L, N, TailleImage, TaillePoints, Titel etc.) pour voir ce qui se passe ! Attention, ne changez qu'un seul a la fois, sauvegardez et executez a nouveau le code avant de changer autre chose !\nN'hesitez pas a nous poser des questions. Passez ensuite a Code06a.py"

TailleImage = 7 # l'image a une longueur de bord de TailleImage pouces
fig = plt.figure( figsize=(TailleImage, TailleImage) )
ax = plt.axes( xlim=( 0, L), ylim=( 0, L)) # Intervalle des axes x et y

TaillePoints = 10.
ax.plot(X, Y, 'o', color='red', markersize = TaillePoints ) # dessine les points de donnees # dessine les points de donnees

Titel = "Positions aleatoires de " + str(N) + "\nparticules dans un carre de longueur de bord " + str(L)
ax.set_title(Titel, fontsize  = 18)
ax.set_xlabel('positions x', fontsize  = 20)
ax.set_ylabel('positions y', fontsize  = 20)

plt.show() # l'image s'ouvre.
