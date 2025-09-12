import util


liste_coord_points = util.gen_points(11, 10.0, 10.0)
liste_points = ["1", "3", "2", "4", "5", "6", "7", "8", "9", "10", "11"]
voisins = util.k_pp_voisins(liste_points, liste_coord_points, 
                            util.calc_nb_voisins_ideal(liste_points),
                         (34.5, 34.5))
print(voisins)