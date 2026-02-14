def endpoint_integral(operacion, n1, n2=0):
    
    if operacion == "suma":
        resultado = n1 + n2
    elif operacion == "resta":
        resultado = n1 - n2
    elif operacion == "multiplicacion":
        resultado = n1 * n2
    elif operacion == "division":
        if n2 != 0:
            resultado = n1 / n2
        else:
            return "Error: División por cero"
    elif operacion == "fibonacci":
        a, b = 0, 1
        secuencia = []
        while len(secuencia) < n1:
            secuencia.append(a)
            a, b = b, a+b
        return secuencia
    elif operacion == "conversion":
        return{
            "numero original": n1,
            "binario": bin(n1).removeprefix("0b"),
            "hexadecimal": hex(n1).removeprefix("0x"),
            }
    else:
        return "Operación no válida"
    
    return operacion, resultado
        
    
    
print(endpoint_integral("fibonacci",5))
print(endpoint_integral("resta", 5,5))
print(endpoint_integral('conversion',15))
    
    
        