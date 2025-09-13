import math
import random as rd

def distance(coord_1, coord_2):
    """
    Entrees: coord_1:tuple[float] et coord_2:tuple[float] : coordonnees des 
             deux points en entree 
    Role: calcule la distance entre deux points en 2D
    Sortie: distance:float
    """
    distance = math.sqrt(
               abs(((coord_2[0] - coord_1[0])**2) + ((coord_2[1] - coord_1[1])**2))
               )
    return distance

def permuter(tableau, indice_1, indice_2):
    """
    Entrees: tableau:list : liste de valeurs mathematiques
             indice_1:int et indice_2:int : deux indices dans tableau
    Sortie: tableau:list
    Role: permute les elements d'indice indice_1 et indice_2 dans tableau
    """
    # permutation
    tableau[indice_1], tableau[indice_2] = tableau[indice_2], tableau[indice_1]
    return tableau

def tri_croissant(liste):
    """
    Entree: liste:list : liste d'elements a valeur mathematique
    Sortie: idem
    Role: trie par ordre croissant, si ce n'etait pas deja assez evident
    """
    for i in range(1, len(liste)):
        element = liste[i]
        j = i - 1
        while j >= 0 and element < liste[j]:
            liste[j + 1] = liste[j]
            j -= 1
        liste[j + 1] = element
    return liste

def trouver_indices(element, liste):
    """
    Entrees: element[any] : un element dont on cherche les indices
             liste:list : une liste d'elements lambda
    Sortie: indices:list[int] : liste des indices de element dans liste
    Role: trouve et renvoie les indices de toutes les apparitions de element 
          dans liste
    """
    indices = []
    for indice in range(len(liste)): # on parcourt tout
        if liste[indice] == element:
            indices.append(indice) # et on ajoute l'indice si il y a 
                                   #correspondance
    return indices

def gen_points(points, max_x, max_y):
    """
    Entrees:
    Role:
    Sortie: liste_finale:list[tuple[tuple[float, float]]] : la liste des c
    oordonnees de tous les points generes et de leurs noms
    """
    liste_finale = [] # On genere une liste vide 
    for i in range(points): # On execute points fois la boucle
        valeur = (rd.uniform(0, max_x), rd.uniform(0, max_y)) # On 
        # genere aleatoirement les coordonnees que l'on place dans le tuple
        #valeur
        liste_finale.append((valeur, "x" + str(i + 1))) # On ajoute valeur a la fin de la liste
    return liste_finale # On renvoie la liste finale

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
        distance_point.append(distance(pos_x, element[0])) # Ajout de chaque 
                                                      #distance a distance_point

    tri_croissant(distance_point)
    for i in range(nb_voisins):
        voisins.append((liste_coord_points[i], 
                        distance_point[i])) # On ajoute a voisins le point selon
                                        #le format : ['nom', (x1, x2), distance]
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