import util


liste_points = util.gen_points(11, 10.0, 10.0)
voisins = util.k_pp_voisins(liste_points, 
                            util.calc_nb_voisins_ideal(liste_points),
                         (34.5, 34.5))
print(voisins)