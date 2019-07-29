import sys
import random
import matplotlib.pyplot as plt

# debut declaration fonction
def distance( Array, IndexA, IndexB, Length):
    dx = abs( Array[IndexA] - Array[IndexB] ) # calcule la valeur absolue de la difference
    dxL = Length - dx
    if ( dx < dxL ):
        distance = dx
        print "La distance la plus courte entre les deux particules est indiquee par la ligne bleue. <------"
    else:
        distance = dxL
        print "La distance la plus courte entre les deux particules est indiquee par la ligne verte. <------"
    return distance
# fin declaration fonction

mot = raw_input("\n******\nNous presentons comment definir nos propres fonctions dans ce code. La distance la plus courte entre les particules est calculee avec une fonction qui prend comme arguments un tableau, deux indices du tableau et une longueur. La fonction est definie de la ligne 6 a la ligne 15 du code. Nous utilisons la fonction dans la ligne 31.\n\nOuvrez le code et essayez de comprendre ce que fait la fonction ! Testez votre comprehension dans Code06c.py\nTappez ENTER pour continuer :")

L = 5.0 # Longueur de la boite
N = 2 # Nombre de particules
print "\n******\nL = ", L
print "N = ", N

# positions x et y aleatoires des particules dans l'intervalle 0...L
X = [ random.uniform(0,L) for i in range(N) ]
Y = [ 1.0 for i in range(N) ]
print "\n******\npositions x aleatoires = ", X
print "positions y aleatoires = ", Y

Distance = distance(X, 0, 1, L) # <------------- Calcul de la distance
print "La distance la plus courte entre les deux particules est", Distance, ".\n"

TailleImage = 7 # l'image a une longueur de bord de TailleImage pouces
fig = plt.figure( figsize=(TailleImage, TailleImage * (2./5) ) )
ax = plt.axes( xlim=( 0, L), ylim=( 0, 2.)) # Intervalle des axes x et y

TaillePoints = 10.
ax.plot(X, Y, 'o', color='red', markersize = TaillePoints ) # dessine les points de donnees
ax.plot( [-1*L,2*L], Y, '-', color = 'lightgreen', linewidth = 4.0 ) # Trace une ligne entre les deux particules.
ax.plot( X, Y, '-', color = 'dodgerblue', linewidth = 4.0  ) # Trace une ligne entre les deux particules.
ax.text( L/2.0, 1.5, 'Quelle couleur indique la distance la plus courte, verte ou bleue ?\nConsultez le texte dans le terminal !', horizontalalignment='center'  )

Titel = "Positions aleatoires de " + str(N) + " particules dans un couloir de longueur " + str(L) + "."
ax.set_title(Titel, fontsize  = 10)
ax.set_xlabel('positions x', fontsize  = 13, labelpad=-6)
ax.set_ylabel('positions y', fontsize  = 13)

plt.show() # l'image s'ouvre.
