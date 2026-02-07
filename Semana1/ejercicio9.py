#NLP Pattern Identifier: Como parte de un motor de procesamiento de lenguaje natural (NLP), 
# se te pide identificar caracteres clave. Crea un script que reciba un solo carácter de 
# texto y determine si pertenece al conjunto de vocales. El programa debe ser robusto
# frente a variaciones de caja, tratando 'A' y 'a' como equivalentes, y devolviendo un valor 
# booleano o un mensaje de confirmación de detección.
#Pista: En lugar de escribir un if gigante con 10 condiciones (a, e, i, o, u en mayúsculas y minúsculas),
#usa el operador in. Ejemplo: if letra.lower() in "aeiou":. Esto hace que tu código sea mucho más legible y profesional.

cont = 0

while cont < 5:
    
    letra = input("Ingrese una letra: ") .strip() .lower()
    if len(letra) == 1 and letra.isalpha():

        if letra.lower() in 'aeiou':
            print("True")
            cont += 1
        else:
            print("False")
            cont += 1
    else:
        print("Entrada no válida. Por favor, ingrese una sola letra.")