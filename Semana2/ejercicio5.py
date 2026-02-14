lista = [15, 20, 16, 150, 10]

umbralcritico = int(input("Ingrese el umbral critico: "))

media = sum(lista) / len(lista)
limite = media * 3
bandera_alerta = False

for valor in lista:
    if valor > limite:
        bandera_alerta = True
        break
    elif umbralcritico < media:
        bandera_alerta = True
        break

if bandera_alerta:
    print("Alerta: Se ha superado el umbral critico o el limite de 3 veces la media.")
else:
    print("Todo está dentro de los límites aceptables.")
    
    