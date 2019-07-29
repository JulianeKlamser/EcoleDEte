import sys
import random
random.seed( a = None )

print "\n******\nTestons si\nR = random.randint( A, B)\ngenere vraiment une distribution uniforme entre\nA <= R <= B\nPour cela, nous allons a nouveau generer N nombres aleatoires dans une boucle for, mais cette fois nous allons stocker les nombres dans un tebleau. Nous choisissons :"

A = 0
B = 5
print "A =", A
print "B =", B
mot = raw_input("Tappez ENTER pour continuer :")

print "\n*****\nNous devons compter combien de fois les entiers dans l'intervalle [", A, ",", B,"] apparaissent en moyenne.\nIl y a au total"

L = A + B + 1
print "L = A + B + 1 =", L, "\nentiers dans cet intervalle. Par consequent, notre tebleau a besoin de", L, "entrees."

mot = raw_input("Tappez ENTER pour continuer :")

print "\n*****\nNous commencons par un tebleau qui a a chaque entree un zero. Nous pouvons generer ce tebleau avec la syntaxe suivante.\nT = [ 0 for i in range(L) ]"

T = [ 0 for i in range(L) ]
print "Cela nous donne T =", T
mot = raw_input("Tappez ENTER pour continuer :")

print "\n****\nComme precedemment, nous generons un nombre aleatoire avec"

a = random.randint(A,B)
print "a = random.randint(A,B)"
print "Cela nous donne a =", a
mot = raw_input("Tappez ENTER pour continuer :")

print "\n*****\nChaque fois que la fonction random.randint(A,B) nous donne" , a,", nous allons augmenter l'entree T[" , a,"] avec"

T [ a ] += 1
print "T [" , a, "] += 1"
print "Cela nous donne T =", T

print "\nNous avons deja prepare une partie du code pour vous dans Code04c.py. Executez Code04c.py et suivez les instructions."
