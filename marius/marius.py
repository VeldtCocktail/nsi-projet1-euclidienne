import random

# attention : renvoyer les points sous forme : [(x1, y1), (x2, y2), ...]

def gen_points(points, max_x, max_y): # On créer la fonction "gen_points"
    """

    """
    liste_finale = [] # On génère une liste vide 
    for i in range(points): # On execute points fois la boucle
        valeur = (random.uniform(0, max_x), random.uniform(0, max_y)) # On 
        # génère aléatoirement les coordonnées que l'on place dans le tuple : "valeur"
        liste_finale.append(valeur) # On ajoute valeur a la fin de la liste
    return liste_finale # On retorune la liste finale

print(gen_points(8, 42.0, 42.0))