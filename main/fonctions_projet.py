import random as rd
import util

# Toutes ces fonctions servent au programme principal.
def k_pp_voisins(liste_coord_points, nb_voisins, pos_x):
    """
    Entrees: liste_points:list[str] : liste des points et leurs 
             coordonnees (en float)
             nb_voisins:int : le nombre de voisins a trouver
             pos_x:tuple[float] : position en 2D du point
             liste_coord_points:list[]
    Role: trouve les nb_voisins plus proches voisins du point de coordonnees   
          pos_x dans la liste de points liste_points
    Sortie: voisins:list[tuple[float]]
    Note: renvoie voisins sous la forme :
    """
    voisins = [] # Liste des nb_voisins plus proches voisins
    distance_point = [] # Liste avec la distance de tous les points dans 
                        #liste_coord_points
    
    for element in liste_coord_points:
        distance_point.append(util.distance(pos_x, element[0])) # Ajout de 
                                                      #chaque distance a 
                                                      #distance_point

    util.tri_croissant(distance_point)
    for i in range(nb_voisins):
        voisins.append((liste_coord_points[i], 
                        distance_point[i])) # On ajoute a voisins le point 
                                            #selon le format :
                                            #['nom', (x1, x2), distance]
    return voisins

def calc_nb_voisins_ideal(liste_points):
    """
    Entree: liste_points:list[any] : liste des points dont on cherche les 
    voisins
    Role: calcule le nombre ideal de voisins a rechercher
    Sortie: nb_voisins:int le nombre ideal de voisins a rechercher
    """
    if len(liste_points) % 2 == 0:
        nb_voisins = len(liste_points) - 1
    else:
        nb_voisins = len(liste_points)
    return nb_voisins

def predire_classe(liste_voisins):
    """
    Entree: liste_voisins:list[tuple[tuple[tuple[float], str, str], float]] :
            liste des voisins du point dont on cherche a predire la classe. 
            Elle contient la position de ces voisins, le nom, leur classe et la 
            distance avec le point dont on cherche a predire la classe.
    Role: predit la classe du point dont on a pas la classe
    Sortie: classe_point:str : la classe predite du point : "C" ou "T"
    """
    liste_classes_voisins = []
    for element in liste_voisins:
        liste_classes_voisins.append(element[0][2])
    apparitions_c = util.compter_element(liste_classes_voisins, "C")
    apparitions_t = util.compter_element(liste_classes_voisins, "T")
    if apparitions_c > apparitions_t:
        classe_point = "C"
    else:
        classe_point = "T"
    return classe_point

# fonction servant aux questions facultatives.
def gen_points(points, max_x, max_y, classes):
    """
    Entrees: points:int : nombre de points a generer
             max_x:float : l'abscisse maximum que peut avoir un point (inclue)
             max_y:float : l'ordonnee maximum que peut avoir un point (inclue)
             classes:tuple[str] : la/les classes possibles des points a generer
    Role: genere points points, aux coordonnees en 2 dimensions, tout en leur
          affectant une classe de facon aleatoire parmi celles proposees dans 
          classe
    Sortie: liste_finale:list[tuple[tuple[float, float]]] : la liste des 
            coordonnees de tous les points generes et de leurs noms
    """
    liste_finale = [] # On genere une liste vide 
    for i in range(points): # On execute points fois la boucle
        valeur = (rd.uniform(0, max_x), rd.uniform(0, max_y)) # On 
        # genere aleatoirement les coordonnees que l'on place dans le tuple
        #valeur
        liste_finale.append((valeur, "x" + str(i + 1), classes[rd.randint(0, 1)
                                                               ]
                             )) # On ajoute valeur a la fin de la liste
    return liste_finale # On renvoie la liste finale