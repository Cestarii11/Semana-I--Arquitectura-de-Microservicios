#DataSet de Sensores: Estás trabajando con un dataset de sensores climáticos que envían datos en grados Celsius,
# pero el motor analítico global requiere la escala Fahrenheit.Implementa un algoritmo que reciba una lista de valores
# flotantes y devuelva una nueva lista con la conversión aplicada mediante la fórmula: F = (C * 9/5) + 32. El reto consiste en 
# procesar la colección completa sin alterar los datos originales (inmutabilidad).Pista: Tienes dos caminos. 
# El básico: crear una lista vacía fahrenheit = [], usar un ciclo for para recorrer la de Celsius y hacer .append() del resultado. 
# El avanzado (Analista Senior): usar una List Comprehension para hacerlo en una sola línea.


celsius_temps = [20.5, 30.0, 15.2, 0.0, 38.5]


fahrenheit_temps = [(temp * 9/5) + 32 for temp in celsius_temps]

print(f"Original (C): {celsius_temps}")
print(f"Convertido (F): {fahrenheit_temps}")