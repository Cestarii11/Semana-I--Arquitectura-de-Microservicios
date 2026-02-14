
estservidor_input = input("¿El servidor está activo? (si/no): ").strip().lower()
tipo = input("Ingrese el tipo de usuario: Premium o Standard:  ").lower().strip()
match estservidor_input:
    case "si":
        estservidor = True
    case "no":
        estservidor = False
match estservidor:
    case True:
        if tipo == "premium":
            print("Tienes permitido un maximo de 1000 peticiones por segundo.")
        elif tipo == "standard":
            print("Tienes permitido un maximo de 100 peticiones.")
    case False:
        print("El servidor está en mantenimiento.")
        print(f'\n Tienes 0 solicitudes')
    case _:
        print("Estado del servidor no reconocido.")