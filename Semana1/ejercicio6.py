opcion = int(input("Selecione el tipo de vehiculo: Pick up (1) Gandola (2) Mudanza (3):  "))
km = float(input("Cuantos Km va a recorrer: "))
preciokm = km*1.5


match opcion:
    case 1:
        base = 6.0
    
    case 2:
        base = 7.0

    case 3:
        base = 10.0
    case _:
        print('ERROR')
        
        
print (f"El precio base es: ${base}")
print (f"El Costo por distancia es: ${preciokm}")
print (f"--------------------------------------------")
print (f"El precio total es:  ${preciokm + base}")
    