import math

def distance(coord_1, coord_2):
    """
    Entrees: coord_1:tuple[float] et coord_2:tuple[float] : coordonnees des 
             deux points en entree 
    Role: calcule la distance entre deux points en 2D
    Sortie: distance:float
    """
    distance = math.sqrt(
               abs(((coord_2[0] - coord_1[0])**2) + (
                   (coord_2[1] - coord_1[1])**2)))
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
    Role: trie par ordre croissant, si ce n'etait pas deja assez evident. Par
          insertion, apparement ca peut etre utile de preciser.
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

def compter_element(liste, element):
    """
    Entrees: liste:list : une liste d'elements quelconques
             element:any : l'element dont on cherche le nombre d'iterations 
             dans liste
    Role: compte er renvoie le nombre de fois que element apparait dans liste
    Sortie: apparitions:int : le nombre d'apparitions de element dans list
    """
    apparitions = 0
    for item in liste: # On parcourt toute la liste, et increment le compteur
                       #si element apparait
        if item == element:
            apparitions += 1
    return apparitions