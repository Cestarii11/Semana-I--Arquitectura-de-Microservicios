token = input("Ingrese una palabra: ")

for letra in token:
    if letra.isdigit():
        break

print(f"El resultado final es: {bool(len(token) > 12) and letra.isdigit() and not token.startswith('TEST')}")

    