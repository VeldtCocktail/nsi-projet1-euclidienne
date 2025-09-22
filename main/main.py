import fonctions_projet as fp

nombre_points = int(input("Combien d'autres points a generer ? "))
abscisse_max = float(input("Abscisse maximale des autres points ? "))
ordonnee_max = float(input("Ordonnee maximale des autres points ? "))
abscisse_point = float(input("Abscisse du point dont on cherche la classe ? "))
ordonnee_point = float(input("Ordonnee du point dont on cherche la classe ? "))

liste_points = fp.gen_points(nombre_points, abscisse_max, ordonnee_max, 
                             ("C", "T"))
voisins = fp.k_pp_voisins(liste_points, 
                            fp.calc_nb_voisins_ideal(liste_points),
                         (abscisse_point, ordonnee_point))

print("La classe du point de coordonnees (" + str(abscisse_point) + ', ' 
      + str(ordonnee_point) + 
      ") sera, selon l'algorithme des plus proches voisins : "
        + fp.predire_classe(voisins))