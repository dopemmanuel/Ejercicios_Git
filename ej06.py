"""Escribe un programa que pida el importe final de un artículo y calcule e imprima por
pantalla el IVA que se ha pagado y el importe sin IVA (suponiendo que se ha aplicado un
tipo de IVA del 10%)."""

importe_final = float(input("Introduce el importe final del artículo: "))
iva = 0.10
importe_sin_iva = importe_final / (1 + iva)
iva_pagado = importe_final - importe_sin_iva
print("IVA pagado:", iva_pagado)
print("Importe sin IVA:", importe_sin_iva)
