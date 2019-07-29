import sys

mot = raw_input("\nVeuillez entrer un nombre entier : ")
nombre = int( mot )

# debut declaration if
if ( (nombre % 2) == 0 ):
    print "\n***\n", nombre, "est pair."
else:
    print "\n***\n", nombre, "est impair."
# fin declaration if

mot = raw_input("\nTapez ENTER pour continuer !")

if ( nombre > 0 ):
    print "\n***\n", nombre, "est superieur a zero."
elif ( nombre < 0 ):
    print "\n***\n", nombre, "est inferieur a zero."
else:
    print "\n***\n", nombre, "est zero."

mot = raw_input("\nTapez ENTER pour continuer !")
mot = raw_input("\nVeuillez entrer un autre nombre entier : ")
nombre2 = int( mot )

if ( (nombre2 >= 0) and (nombre >= 0) ):
    print "\n***\n", nombre2, "et", nombre, "sont superieurs ou egaux a zero."
elif ( (nombre2 >= 0) or (nombre >= 0) ):
    print "\n***\n", nombre2, "ou", nombre, "est superieur ou egal a zero."
    if (  (nombre2 >= 0) ):
        print nombre2, "est superieur ou egal a zero et", nombre, "est inferieur a zero."
    else:
        print nombre, "est superieur ou egal a zero et", nombre2, "est inferieur a zero."
else:
    print "\n***\n", nombre2, "et", nombre, "sont inferieurs a zero."
mot = raw_input("\nTapez ENTER pour continuer !")

print "\n*****\nCe code utilise les 'declarations if'. Une 'declarations if' verifie si une condition donnee est remplie ou non.\nVoici quelques exemples de conditions :\n A == B : A egal B\n A != B : A different de B\n A < B : A plus petit que B\n A > B : A plus grand que B\n A >= B : A superieur ou egal a B\n A <= B : A inferieur ou egal a B\n ( A + B ) < 19 : la somme est inferieure a 19\n etc.\nUne partie du code n'est executee que si la condition est vraie.\nExecutez le code plusieurs fois avec des numeros differents. Selectionnez egalement les nombres negatifs et zero.\nApres cela, ouvrez le code et essayez de comprendre comment il fonctionne. Notez qu'elif signifie autrement si (else if).\nApres, vous pouvez tester avec Code02d.py si vous avez compris les 'declarations if'.\n\n"
