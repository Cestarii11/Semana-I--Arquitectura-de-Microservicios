caracter =input("Ingresa un mensaje: ").strip()
suma = sum(ord(char) for char in caracter)

if suma % 2 == 0:
    print("El mensaje es par")
    print(f"La suma de los valores ASCII es: {suma}")
else:
    print("El mensaje es impar")
    print(f"La suma de los valores ASCII es: {suma}")

