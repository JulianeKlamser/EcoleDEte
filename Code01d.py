
a = 5
b = 2
print "\n****\na = ", a
print "b = ", b
print "a / b =", a / b
print "a / float(b) =", a / float(b)
print "Il est possible de transformer un int en float. La transformation ci-dessus, n'a pas change le type de la variable b : b = ", b , "(b est toujours un int)"
mot = raw_input("\nTapez Enter pour continuer !")

b = float( b )
print "\n*****\nPour changer le type de la variable b, il faut utiliser la syntaxe suivante :\nb = float( b )\nLe resultat pour b est maintenant : b = ", b
mot = raw_input("\nTapez Enter pour continuer !")

print "\n****\na = ", a
print "b = ", b
print "a / b =", a / b
print "a / int(b) =", a / int(b)
print "La transformation inverse est egalement possible. On peut transformer un float en un int. Encore, la transformation ci-dessus, n'a pas change le type de la variable b : b = ", b , "(b est toujours un float)"
mot = raw_input("\nTapez Enter pour continuer !")

b = int( b )
print "\n*****\nEncore, pour changer le type de la variable b, il faut utiliser la syntaxe suivante :\nb = int( b )\nLe resultat pour b est maintenant : b = ", b
mot = raw_input("\nTapez Enter pour continuer !")

print "\n*****\nNous avons aussi le type de donnees str. str signifie string (chaine de caracteres). On peut simplement dire que les str (chaines de caracteres) sont des mots.\nBien sur, les operations mathematiques avec des mots ne sont pas possibles !\nPar exemple, str(5.0)/str(2.0) est tout aussi inutile que chat/chien !!!"
mot = raw_input("\nTapez Enter pour continuer !")

print "\n*****\nOn peut assigner des chaines de caracteres a des  variables. Executez code01e.py et suivez les instructions.\n"
