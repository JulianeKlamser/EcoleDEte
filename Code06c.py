import sys
import random
import matplotlib.pyplot as plt

# debut declaration fonction
def distance( Array, IndexA, IndexB, Length):
    dx = abs( Array[IndexA] - Array[IndexB] ) # calcule la valeur absolue de la difference
    dxL = Length - dx
    if ( dx < dxL ):
        distance = dx
        print "La distance la plus courte est indiquee par la ligne bleue. <------"
    else:
        distance = dxL
        print "La distance la plus courte est indiquee par la ligne verte. <------"
    return distance
# fin declaration fonction

L = 5.0 # Longueur de la boite
N = 4 # Nombre de particules
print "\n****\nL =", L, "et N =", N

X = [ ( L / 2.0 ) for i in range(N) ] # Ceci cree un tableau avec 4 entrees, toutes sont L/2.
X[0] = random.uniform(0,L) # position aleatoire pour la position x de la particule 0
X[1] = random.uniform(0,L) # position aleatoire pour la position x de la particule 1
Y = [ ( L / 2.0 ) for i in range(N) ] # Ceci cree un tableau avec 4 entrees, toutes sont L/2.
Y[2] = random.uniform(0,L) # position aleatoire pour la position y de la particule 2
Y[3] = random.uniform(0,L) # position aleatoire pour la position y de la particule 3
print "positions x aleatoires = ", X
print "positions y aleatoires = ", Y

ParticuleA = 0
ParticuleB = 1
print "\nHorizontale -> La distance la plus courte entre particule", ParticuleA, "et", ParticuleB, ":"
dist = distance(X, ParticuleA, ParticuleB, L) # <------------- Calcul de la distance
print "La distance la plus courte entre les deux particules est", dist, ".\n"

print "\nExercice : Repetez ce calcul de la distance pour les particules verticales (indices 2 et 3) en utilisant la meme fonction (vous devez choisir des arguments differents pour la fonction) ! Essayez de resoudre le probleme vous-meme avant de comparer avec la solution (Code06cSolution.py)."

TailleImage = 7
fig = plt.figure( figsize=(TailleImage, TailleImage) )
ax = plt.axes( xlim=( 0, L), ylim=( 0, L))

TaillePoints = 10.
ax.plot(X, Y, 'o', color='red', markersize = TaillePoints ) # dessine les points de donnees
# lignes horizontales
ax.plot( [0, L], [(L / 2), (L / 2)], '-', color = 'lightgreen', linewidth = 4.0 )
ax.plot( [X[0], X[1]], [(L / 2), (L / 2)], '-', color = 'dodgerblue', linewidth = 4.0 )
# lignes verticales
ax.plot( [(L / 2), (L / 2)], [0, L], '-', color = 'lightgreen', linewidth = 4.0 )
ax.plot( [(L / 2), (L / 2)], [Y[2], Y[3]], '-', color = 'dodgerblue', linewidth = 4.0 )
ax.text( L/2.0, 1.5, 'Quelle couleur indique la distance la plus courte, verte ou bleue ?\nConsultez le texte dans le terminal !', horizontalalignment='center'  )


Titel = "Positions de " + str(N) + "\nparticules dans un carre de longueur de bord " + str(L)
ax.set_title(Titel, fontsize  = 18)
ax.set_xlabel('positions x', fontsize  = 20)
ax.set_ylabel('positions y', fontsize  = 20)

mot = raw_input("\nTappez ENTER pour continuer :")
plt.show() # l'image s'ouvre.
