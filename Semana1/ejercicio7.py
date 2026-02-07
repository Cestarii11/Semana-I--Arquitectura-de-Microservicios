while True:
    opcion = int(input("Elija el metodo de pago: Pago movil (1) o Tarjeta (2):  "))

    match opcion:
        case 1:
            clave = (input("Escriba su clave: "))
            if len(clave) == 8 and clave.isdigit():
                print("Clave Valida")
                break
            else:
                print("Clave Invalida")
            
        
        case 2:
            clave = (input("Ingrese la clave de su tarjeta: "))
            if len(clave) == 10 and clave.isdigit():
                print("Clave valida")
                break
                
            else:
                print("Clave invalida!")
        case _:
            print("Opcion no valida!")
            
            
    