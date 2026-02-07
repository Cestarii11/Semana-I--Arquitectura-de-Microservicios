# Ejercicio 2: Solicitar al usuario su nombre y cargo, y mostrar un mensaje de bienvenida.

nombre = input("Ingrese su nombre: ").strip().capitalize() #Poner la primera letra en mayúscula y eliminar espacios
cargo = input("Ingrese su cargo: ")
mensaje = f"Acceso-concedido: Bienvenido {nombre}, al sistema de {cargo}"
print(mensaje)