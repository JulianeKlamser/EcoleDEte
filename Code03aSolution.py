import sys

A = 0
B = 100
print "\n****\nJouez a ce jeu avec votre voisine. Pensez a un nombre entier entre", A, "et", B, "."
mot = raw_input("Entrez le nombre sans dire le nombre a votre voisine. : ")
nombre = int( mot )


for i in range(30):
    print "\n"

print "********---->\n\nDemandez a votre voisine de deviner votre nombre entier entre", A, "et", B, ". Laissez l'ordinateur decider si la devinette etait correcte. "
mot_2 = raw_input("Votre voisine saisit le nombre ici : ")
nombre_2 = int( mot_2 )

# Ce qui suit est une boucle "while". Elle est executee encore et encore, jusqu'a ce que la condition apres le "while" soit satisfaite.
essais = 1 #<-------------------- Solution 1/3
while( nombre_2 != nombre ):
    essais += 1 #<-------------------- Solution 2/3
    print "\nVotre voisine n'a pas bien devine."
    
    if ( nombre > nombre_2 ):
        print "* > * Le nombre est superieur a", nombre_2
        mot_2 = raw_input("Essayez a nouveau :")
    else:
        print "* < * Le nombre est inferieur a", nombre_2
        mot_2 = raw_input("Essayez a nouveau :")
    nombre_2 = int( mot_2 )


print "\n\n*****\nFelicitations, vous avez trouve le bon nombre. C'etait ", nombre_2, "!\n----->Il vous a fallu", essais, "essais pour deviner le nombre.\n\n" #<-------------------- Solution 3/3

print "Excercice : Maintenant, ouvrez le code et essayez de le comprendre (les commentaires vous aideront). Creez une variable qui compte le nombre total d'essais. Essayez-le sans consulter la solution du Code03aSolution.py\nApres avoir reussi, executez Code03b.py !\n\n"
