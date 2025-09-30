"""Escribe un programa que pida el importe sin IVA de un artículo y el tipo de IVA a aplicar
y calcule e imprima por pantalla el precio final del artículo. 
"""
importe_sin_iva = float(input("Ingrese el importe sin IVA: "))
tipo_iva = float(input("Ingrese el tipo de IVA a aplicar (en %): "))
precio_final = importe_sin_iva + (importe_sin_iva * tipo_iva / 100)
print("El precio final del artículo es:", precio_final)
