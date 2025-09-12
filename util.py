import math

def distance(coord_1, coord_2):
    """
    Entrees: coord_1:tuple[float] et coord_2:tuple[float] : coordonnees des 
             deux points en entree 
    Role: calcule la distance entre deux points en 2D
    Sortie: distance:float
    """
    distance = math.sqrt(abs((coord_1[0] - coord_2[0])**2 + (coord_1[1] - coord_2[1])**2))
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

def triCroissant(liste):
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

def trouverIndices(element, liste):
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