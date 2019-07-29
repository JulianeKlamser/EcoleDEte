import sys
import random
random.seed( a = None )

A = 0
B = 5
print "\n*****\nA =", A
print "B =", B

L = A + B + 1
print "L =", L

T = [ 0 for i in range(L) ]
print "Cela nous donne T =", T

N = 100000
for i in range( N ):
    a = random.randint( A, B)
    T[ a ] += 1

print "\nT =", T

total = 0
for i in range( L ):
    total += T[ i ]

print "On parle d'une distribution uniforme, si chaque valeur a la meme probabilite d'apparaitre et cette probabilite est simplement donnee par 1/L, ou L est le nombre total de valeurs possibles. Pour\nL =", L,"\n1/float(L) =", 1/float(L)

for i in range( L ):
    T[ i ] /= float(total)
    print "La probabilite que le resultat de random.randint( A, B) soit", i, "est de", T[ i ], "."




