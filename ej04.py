"""Escribe un programa que le pida al usuario una temperatura en grados Celsius, la
convierta a grados Fahrenheit e imprima por pantalla la temperatura convertida. 
"""
celcius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = (celcius * 9/5) + 32
print("La temperatura en grados Fahrenheit es:", fahrenheit)
