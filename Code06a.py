import sys
import random
import matplotlib.pyplot as plt

def distance(X, ParticulA, ParticulB, L):
    dx = abs( X[ParticulA] - X[ParticulB] ) # calcule la valeur absolue de la difference
    dxL = L - dx
    if ( dx < dxL ):
        distance = dx
        print "La distance la plus courte entre les deux particules est" , distance,"et indiquee par la ligne bleue. <------"
    else:
        distance = dxL
        print "La distance la plus courte entre les deux particules est" , distance,"et indiquee par la ligne verte. <------"
    return distance


L = 5.0 # Longueur de la boite
N = 2 # Nombre de particules


print "\n****\nVous souvenez-vous du couloir avec les deux portes, qui etait un piege malefique ? Il faut qu'on y revienne.\nImaginez qu'il y a deux personnes dans ce couloir. Nous voulons calculer la distance la plus courte entre les deux personnes pour toutes les positions possibles d'elles dans le couloir. L'extremite gauche du corridor est a x = 0 et l'extremite droite est a x = L.\nNous choisissons :\nN =", N, "(nombre de personnes dans le corridor)\nL =", L, "(longueur du corridor)"
mot = raw_input("Tappez ENTER pour continuer :")

# positions x et y aleatoires des particules dans l'intervalle 0...L
X = [ random.uniform(0,L) for i in range(N) ]
Y = [ 1.0 for i in range(N) ]
print "\n******\npositions x aleatoires = ", X
print "positions y aleatoires = ", Y

Distance = distance(X, 0, 1, L) # <------------- Calcul de la distance
mot = raw_input("\nLa distance la plus courte est indiquee en bleu ou en vert. Executez le code encore et encore jusqu'a ce que vous voyez les deux possibilites. Continuez ensuite directement avec Code06b.py !\nAppuyez sur ENTER pour dessiner l'image avec les 'personnes' et les lignes.:")

TailleImage = 7 # l'image a une longueur de bord de TailleImage pouces
fig = plt.figure( figsize=(TailleImage, TailleImage * (2./5) ) )
ax = plt.axes( xlim=( 0, L), ylim=( 0, 2.)) # Intervalle des axes x et y

TaillePoints = 10.
ax.plot(X, Y, 'o', color='red', markersize = TaillePoints ) # dessine les points de donnees
ax.plot( [ 0, L], Y, '-', color = 'lightgreen', linewidth = 4.0 ) # Trace une ligne entre les deux particules.
ax.plot( X, Y, '-', color = 'dodgerblue', linewidth = 4.0  ) # Trace une ligne entre les deux particules.
ax.text( L/2.0, 1.5, 'Quelle couleur indique la distance la plus courte, verte ou bleue ?\nConsultez le texte dans le terminal !', horizontalalignment='center'  )

Titel = "Positions aleatoires de " + str(N) + " particules dans un couloir de longueur " + str(L) + "."
ax.set_title(Titel, fontsize  = 10)
ax.set_xlabel('positions x', fontsize  = 13, labelpad=-6)
ax.set_ylabel('positions y', fontsize  = 13)

plt.show() # l'image s'ouvre.
