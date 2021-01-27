#Faça um Programa que peça a temperatura em graus Celsius, 
# transforme e mostre em graus Fahrenheit.

c = float(input('Digite a temperatura: '))
f = (c * 9/5) + 32
print(f'A temperatura em graus Fahrenheit é {f:.1f} ºF')