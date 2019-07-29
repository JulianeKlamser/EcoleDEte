import random
import matplotlib.pyplot as plt
import math

def dist( X, Y, L, pA, pB):
	dx = abs( X[pA] - X[pB] )
	dx = min( L - dx, dx )

	dy = abs( Y[pA] - Y[pB] )
	dy = min( L - dy, dy )
	
	return math.sqrt( dx**2 + dy**2 )

L = 5.0 # Longueur de la boite
N = 2 # Nombre de particules
print "\n****\nL =", L, "et N =", N

# positions x et y aleatoires des particules dans l'intervalle 0...L
X = [ random.uniform(0,L) for i in range(N) ]
Y = [ random.uniform(0,L) for i in range(N) ]
print "positions x aleatoires = ", X
print "positions y aleatoires = ", Y

print "La distance la plus courte entre les deux particules est", dist( X, Y, L, 0, 1)

TailleImage = 7 # l'image a une longueur de bord de TailleImage pouces
fig = plt.figure( figsize=(TailleImage, TailleImage) )
ax = plt.axes( xlim=( 0, L), ylim=( 0, L)) # Intervalle des axes x et y

TaillePoints = 10.
ax.plot(X, Y, 'o', color='red', markersize = TaillePoints ) # dessine les points de donnees

Titel = "Positions de " + str(N) + "\nparticules dans un carre de longueur de bord " + str(L)
ax.set_title(Titel, fontsize  = 18)
ax.set_xlabel('positions x', fontsize  = 20)
ax.set_ylabel('positions y', fontsize  = 20)

mot = raw_input("\nTappez ENTER pour continuer :")
plt.show() # l'image s'ouvre.
