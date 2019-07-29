import sys
import random

random.seed( a = None )


A = 0
B = 100
print "\n****\nDonnez un nombre entier entre", A, "et", B, "."
mot = raw_input("Entrez le nombre ici : ")
nombre = int( mot )

computer = random.randint( A, B)
essais = 1
while( computer != nombre ):
    essais += 1
    if ( nombre > computer ):
        print "* > * L'ordinateur a choisi un nombre trop petit :", computer, "\nNous choisissons", computer, " comme nouvelle limite inferieure pour les nombres aleatoires."
        A = computer
    elif (nombre < computer):
        print "* < * L'ordinateur a choisi un nombre trop grand :", computer, "\nNous choisissons", computer, " comme nouvelle limite superieure pour les nombres aleatoires."
        B = computer
    computer = random.randint( A, B)
    mot = raw_input("Tapez ENTER pour continuer! ")

print "\n\n*****\nL'ordinateur a trouve le bon nombre. C'etait ", computer, "!\n----->Il a fallu", essais, "essais a l'ordinateur pour deviner le nombre.\n\n" #<-------------------- Solution 3/3

