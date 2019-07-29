import sys
import random
random.seed( a = None )

A = 0
B = 5
print "\nA =", A
print "B =", B

L = A + B + 1
print "L =", L

T = [ 0 for i in range(L) ]
print "Cela nous donne T =", T

N = 3
for i in range( N ):
    print "modifiez ici"

print "\nT =", T

print "\n****\nExercice 1 : Remplacer 'print modifiez ici' dans la boucle for avec votre propre code. A chaque iteration de la boucle for, calculez un nombre aleatoire avec a = random.randint( A, B) et augmenter T[ a ] de un ([ T[ a ] += 1).\nExercice 2 : Augmenter N, par exemple N = 10000, et verifiez que chaque entree en T est approximativement la meme apres la boucle for. Cela confirme-t-il que la fonction random.randint( A, B) cree une distribution uniforme des entiers dans l'intervalle A, 1, 2, 3,...,B ?\nEssayez de resoudre le probleme vous-meme d'abord, avant de comparer avec le resultat dans Code04cSolution.py ----->Cette fois, il est obligatoire d'executer Code04cSolution.py a la fin.\nContinuez ensuite avec le Code05a.py\n"
