
cont= 0

while cont < 5:


    numero = int(input("Ingrese un número entero: "))

    suma = 0

    for i in range(1,numero):
        if numero % i == 0:
            suma += i
            
            
    if suma == numero:
        print(f"{numero} es un número perfecto.")
        
    else:
        print(f"{numero} no es un número perfecto.")
        
    cont += 1

        