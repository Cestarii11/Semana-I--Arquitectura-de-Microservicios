cont = 0

while cont < 5:

    a1 = float(input("Ingrese el primer angulo: "))
    a2 = float(input("Ingrese el segundo angulo: "))
    a3 = float(input("Ingrese el tercer angulo: "))
    
    triangulo = a1 + a2 + a3 
    
    if triangulo == 180:
        if a1 == a2 and a1 == a3:
            print(f"Es un triangulo equilatero")
        elif a1 == a2 and a2 != a3 or a2==a3 and a1 != a3 or a1 == a3 and a3 != a2:
            print(f"Es un triangulo isosceles")
        elif a1 != a2 and a2 != a3 and a3 != a1:
            print(f"Es un triangulo escaleno")
    else:
        print("Los angulos no forman un triangulo")
            
    if a1 == 90 or a2 == 90 or a3 == 90:
        print (f"El triangulo incluye un angulo recto 90° ")