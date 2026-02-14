import math

def estan_cerca(x1, y1, x2, y2):

    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    

    return distancia < 10


nodo_a = (0, 0)
nodo_b = (6, 8) 

print(f"¿Están cerca?: {estan_cerca(nodo_a[0], nodo_a[1], nodo_b[0], nodo_b[1])}")