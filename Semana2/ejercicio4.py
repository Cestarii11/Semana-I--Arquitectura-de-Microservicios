def decimal_a_binario(n):
    if n == 0:
        return "0"
    
    binario = ""
    temp_n = n
    while temp_n > 0:
        residuo = temp_n % 2
        binario = str(residuo) + binario  
        temp_n = temp_n // 2
    return binario

def decimal_a_hexadecimal(n):
    if n == 0:
        return "0"
    
    # Mapa de valores para hexadecimal
    digitos_hex = "0123456789ABCDEF"
    hexadecimal = ""
    temp_n = n
    
    while temp_n > 0:
        residuo = temp_n % 16
        hexadecimal = digitos_hex[residuo] + hexadecimal
        temp_n = temp_n // 16
    return hexadecimal

# --- Prueba del Convertidor ---
numero = int(input("Introduce un número decimal para convertir: "))

print(f"\nResultados para el número: {numero}")
print(f"Protocolo Binario: {decimal_a_binario(numero)}")
print(f"Protocolo Hexadecimal: 0x{decimal_a_hexadecimal(numero)}")
