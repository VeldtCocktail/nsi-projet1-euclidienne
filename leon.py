import util

def k_voisins(liste_points, liste_coord_points, nb_voisins, pos_x):
    """
    Entrees: liste_points:list[str] : liste des points et leurs 
             coordonnees (en float)
             nb_voisins:int : le nombre de voisins a trouver
             pos_x:tuple[float] : position en 2D du point
             liste_coord_points:list[]
    Role: trouve les nb_voisins plus proches voisins du point de coordonnees
          pos_x dans la liste de points liste_points
    Sortie: voisins:list[tuple[float]]
    """
    voisins = []
    distance_point = []
    for element in liste_coord_points:
        distance_point.append(util.distance(pos_x, element))
    util.triCroissant(distance_point)
    for i in range(nb_voisins):