"""Escribe un programa para pedirle al usuario las horas de trabajo y el precio por hora y
calcule el importe total del servicio. """

horas = float(input("Ingrese las horas de trabajo: "))
precio_por_hora = float(input("Ingrese el precio por hora: "))
importe_total = horas * precio_por_hora
print("El importe total del servicio es:", importe_total)
