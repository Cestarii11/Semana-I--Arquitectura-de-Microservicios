def es_perfecto(n):
    suma = 0
    for i in range(1, n):
        if n % i == 0:
            suma += i
    return suma == n


cont= 0

while cont < 5:


    numero = int(input("Ingrese un número entero: "))
    
    if es_perfecto(numero):
        print(f"{numero} es un número perfecto.")
        
    else:
        print(f"{numero} no es un número perfecto.")
        
    cont += 1