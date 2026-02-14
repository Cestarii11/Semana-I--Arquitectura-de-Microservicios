#1. API Health-Check Validator: En una arquitectura de microservicios, un "Health Check" determina si un servicio está apto para recibir tráfico. 
# Implementa una función que reciba tres variables: latencia (ms), uso_cpu (%) y estado_db (booleano). El sistema debe devolver un único valor 
# booleano True solo si la latencia es menor a 200ms, el CPU está por debajo del 80% y la base de datos está conectada; de lo contrario, devuelve 
# False.
#Pista: Usa operadores lógicos (and, <, ==) para transformar estas condiciones de negocio en una sola línea de retorno booleano.

def health_check(latencia, uso_cpu, estado_db):
    return latencia<200 and uso_cpu<80 and estado_db == True

latencia = float(input("Ingrese la latencia en ms: "))
uso_cpu = float(input("Ingrese el uso de CPU en %: "))
estado_db_input = input("¿La base de datos está conectada? (si/no): ").strip().lower()
estado_db = estado_db_input == "si"
resultado = health_check(latencia, uso_cpu, estado_db)
print(f"El resultado del Health Check es: {resultado}")