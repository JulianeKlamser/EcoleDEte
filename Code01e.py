import sys

a = "Je m'appelle "
b = ", et j'ai "
c = "ans."
mot = raw_input("\nVeuillez entrer votre nom et tapez enter : ")
mot2 = raw_input("Veuillez entrer votre age et tapez enter : ")
age = int(mot2)

print "\n*****\n", a, mot, b, mot2, c
print "J'aurai", age + 2, "ans en 2021."

print "\nExercice : Ouvrez le code et decouvrez comment votre age en 2021 a ete calcule. Changez le code, de sorte que vous puissiez entrer n'importe quelle annee dans le futur et que le code calcule votre age pour cette annee.\nUne fois que vous avez reussi, executez Code01f.py\n\n"
