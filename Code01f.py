

print "\n\n*******\nL'operateur modulo : \nNous allons decouvrir un nouvel operateur dont vous n'avez probablement jamais entendu parler. Vous connaissez le +, le -, le *, et le /. Maintenant, nous allons rencontrer l'operateur -----> % <----- !\nRegardons quelques exemples : "
mot = raw_input("Tapez Enter pour continuer !")

print "\n*******\nExample 1, L'operateur modulo applique aux int :"
a = 5
b = 2
c = a / b
d = a % b
print "a = ", a
print "b = ", b
print "c = a / b =", c
print "d = a % b =", d
print "L'operation modulo trouve le reste apres division d'un nombre par un autre. "
mot = raw_input("Tapez Enter pour continuer !")

print "\n*******\nExample 2, L'operateur modulo applique aux float :"
A = 5.69
b = 1
c = A / b
d = A % b
print "A = ", A
print "b = ", b
print "c = A / b =", c
print "d = A % b =", d
print "Le comportement de l'operateur modulo est plus complexe lorsqu'il est applique sur un float."
mot = raw_input("Appuyez sur Enter pour voir l'explication.")
print "\n*******\nImaginez que vous etes dans un couloir de L = 10 metres de long. Il y a des portes a chaque extremite du couloir. Nous supposons que la porte gauche est a x = 0.0 et que la porte droite est a x = 10.0.\nMaintenant vous essayez de prendre la porte droite a x = 10.0 et vous entrez a nouveau dans un couloir. Vous supposerez que vous etes dans un nouveau couloir et que votre position est x > L.\nCependant, malheureusement, le couloir est un piege malefique : Vous etes toujours dans le meme couloir et vous venez de passer la porte a x = 0.0, si vous vous tenez dans la porte ouverte a droite (x = 10.0) et que vous regardez la porte a gauche (x = 0.0), vous pouvez vous voir entrer dans le couloir. o.O\nVous pouvez courir sur 100 km a droite ou a gauche, mais vous ne pourrez jamais quitter le couloir de L = 10 metres de long.\nRendons les choses plus concretes.\n"
mot = raw_input("Tapez Enter pour continuer !")
x = 11.2
L = 10
print "\n*******\nVous faites un pas par la porte de droite (situee a x =", L,"). Vous supposez maintenant que votre position est x =", x, ", par example.\nDemandons a l'operateur modulo si votre supposition est correcte ! (rappel: L =", L ,")\nx % L =", x % L, "\nDonc, en fait, votre position est x =", x % L
mot = raw_input("Tapez Enter pour continuer !")
x = -1.2
L = 10
print "\n*******\nVous faites un pas par la porte de gauche (situee a x =", 0,"). Vous supposez maintenant que votre position est x =", x, ", par example.\nDemandons a l'operateur modulo si votre supposition est correcte ! (rappel: L =", L ,")\nx % L =", x % L, "\nDonc, en fait, votre position est x =", x % L
mot = raw_input("Tapez Enter pour continuer !")

print "\n*******\nLisez ce texte plusieurs fois pour vous assurer de bien comprendre l'operateur modulo. Ce sera important plus tard. Vous pouvez jouer avec l'operateur modulo dans le code (Code01g.py) suivant (Executez Code01g.py et suivez les instructions !).  "
