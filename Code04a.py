import sys
print "\n******\nNous allons apprendre a connaitre les tableaux maintenant. Une programmeuse parlerait plus des arrays. Il y a plusieurs facons de declarer un tableau. Par exemple\nA = [ 1, 44, 9, 33, 0]"

A = [ 1, 44, 9, 33, 0]
mot = raw_input("Appuyez sur ENTER pour continuer !")

print "\n******\nCe tableau a la longueur (length) :"

L = len(A)
print "L = len(A) =", L
mot = raw_input("Appuyez sur ENTER pour continuer !")

print "\n******\nMaintenant nous pouvons imprimer toutes les entrees du tableau dans une boucle for :"

for i in range(L):
    print "A[",  i,"] =", A[i]
print "Notez que la numerotation commence par 0 et se termine par (L - 1)!!"
mot = raw_input("Appuyez sur ENTER pour continuer !")

print "\n*****\nNous pouvons modifier les entrees, par exemple comme"

A[ 0 ] = 34902
print "A[" , 0, "] =", A[0]
mot = raw_input("Appuyez sur ENTER pour continuer !")

print "\n*****\nLe tableau est maintenant:"
for i in range(L):
    print "A[",  i,"] =", A[i]
mot = raw_input("Appuyez sur ENTER pour continuer !")

print "\n*****\nUne autre facon de declarer un tableau est :\nB = [ 1 for i in range(4)]"

B = [ 1 for i in range(4)]

print "Nous pouvons imprimer le tableau simplement avec :\nprint B\nCa nous donne : "
print B
mot = raw_input("Appuyez sur ENTER pour continuer !")

print "\n*****\nNous pouvons ajouter des entrees a un tableau :\nB.append(2)"
B.append(2)
print "Ca nous donne B =", B
mot = raw_input("Appuyez sur ENTER pour continuer !")

print "\n*****\nExecutez Code04b.py et suivez les instructions.\n"

