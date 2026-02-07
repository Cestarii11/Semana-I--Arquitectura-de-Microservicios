producto = input("Ingrese el nombre del producto: ").strip().capitalize()
cantidad = int(input("Ingrese la cantidad: "))
precio= float(input("Ingrese el precio unitario del producto: "))

print(f"Venta de {producto}: {cantidad} unidades a un precio de ${precio} cada una")
print(f"Total a pagar ${cantidad*precio}")