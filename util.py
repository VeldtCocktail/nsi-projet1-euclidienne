import math

def distance(x1:float, x2:float, y1:float, y2:float):
    """
    Entrees:
    Role:
    Sortie: distance:float
    """
    distance = math.sqrt(abs((y1 - y2)**2 + (x1 - x2)**2))
    return distance