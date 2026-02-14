def tiempo_espera_fibonacci(n):
    if n <= 0:
        return 0
    if n == 1 or n == 2:
        return 1
    

    serie = [1, 1]
    

    for i in range(2, n):
        siguiente = serie[-1] + serie[-2]
        serie.append(siguiente)
    
    return serie[-1]


print(f"Espera para el reintento 5: {tiempo_espera_fibonacci(3)}s")