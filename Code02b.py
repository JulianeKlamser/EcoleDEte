import sys

mot = raw_input("\nVeuillez entrer un nombre entier positif entre 1 et 5 (appuyez sur enter apres) :")
nombre = int( mot )

print "\n*****\nLes nombres entre 0 et ", nombre, " sont:"
# Debut de la boucle for
for i in range( nombre ):
    print i #L'espace vide avant print doit etre cree avec la touche Tab !!!!
# Fin de la boucle for

print "\n*****\nEt la somme est calculee ici:"
total = 0
for i in range( nombre ):
    total = total + i
    print i, " ;la somme est ",  total

print "\n******\nOuvrez le code et essayez de comprendre la boucle for.\nComprenez-vous comment fonctionne le calcul de la variable 'total' ?\nExercice : Modifiez le code de telle sorte que vous calculiez egalement le produit des nombres.\nApres avoir reussi, continuez avec Code02c.py !\n"
