import sys

print "\n*****\nQu'est-ce qu'une boucle 'for' ?"

mot = raw_input("\nVeuillez entrer un nombre entier positif entre 5 et 15 (appuyez sur enter apres) : ")
nombre = int(mot)

print "\n*****\nMaintenant, nous voulons imprimer tous les nombres qui sont positifs et plus petits que votre entree. Pour cela, nous utiliserons la boucle 'for'."
mot = raw_input("Appuyez sur enter pour continuer.")

print "\n*****\nLes nombres entre 0 et ", nombre, " sont:\n"
for i in range( nombre ):
    print i

mot = raw_input("\nAppuyez sur enter pour continuer.")
print "\n*****\nAvant de consulter le code, jouons encore un peu! Nous voulons aussi imprimer la somme des nombres imprimes."
mot = raw_input("Appuyez sur enter pour continuer.")

print "\n*****\nLe resultat est: \n"
total = 0
for i in range( nombre ):
    total = total + i
    print i, " ;la somme est ",  total

print "\nMaintenant, lancez et ouvrez Code02b.py et essayez de comprendre la boucle for.\n\n"
