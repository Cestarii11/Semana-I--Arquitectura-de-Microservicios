#Calculo de ganancia: Como analista junior, debes calcular la ganancia neta de un producto. 
# Solicita el "Precio de Venta" y el "Costo de Fabricación". Resta el costo del 
# precio y muestra el resultado. Asegúrate de usar números con decimales (float) para que
# el cálculo sea exacto para la contabilidad.


precioVenta = float(input("Ingrese el precio de venta del producto: "))
precioCosto = float(input("Ingrese el costo de la venta del producto: "))

resultado = precioVenta - precioCosto
s = f"{resultado:.3f}".rstrip('0').rstrip('.') # Formatear el resultado para eliminar ceros innecesarios
print(f"La ganancia de la venta es: {s}")

