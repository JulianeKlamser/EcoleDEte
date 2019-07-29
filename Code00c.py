import sys
# <----- python est vraiment puissant. Il sait faire beaucoup de choses. Il suffit de dire a python quelle librairie il doit consulter pour comprendre nos commandes. Par exemple la commande de lecture est conservee dans la librairie sys. Nous devons donc importer la librairie sys!!!! (Voir premiere ligne.)

print "\n\n*******\nVous avez vu qu'il est possible de donner une nouvelle entree au code, alors qu'il est en cours d'execution. Par exemple, comme ceci."


mot = raw_input("\n\nVeuillez entrer votre nom et tapez enter : ")
mot2 = raw_input("\n\nVeuillez entrer votre date de naissance et tapez enter : ")

print "\n\n*******\n",mot, "est nee le", mot2, " !\n\n"

mot = raw_input("Vous pouvez egalement utiliser la commande de lecture pour mettre le code en pause, tout comme ici. Tapez Enter pour continuer !\n")


print "\n\n*******\Excersice : Laissez le code lire votre age et imprimer la phrase : XYZ a x ans.\nN'oubliez pas de sauvegarder le code modifie avant de le lancer !\n\nContinuez ensuite avec Code01a.py\n\n"
