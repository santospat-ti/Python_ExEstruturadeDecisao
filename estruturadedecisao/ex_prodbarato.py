"""Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
sabendo que a decisão é sempre pelo mais barato."""
import time

print(f'Bem-vindo!')
time.sleep(0.8)
print('-'*30)
print()
produto1 = float(input('Qual o valor do primeiro produto? R$ '))
produto2 = float(input('Qual o valor do segundo produto? R$ '))
produto3 = float(input('Qual o valor do terceiro produto? R$ '))

barato = ''
if produto1 < produto2 and produto1 < produto3:
    barato = produto1
elif produto2 < produto1 and produto2 < produto3:
    barato = produto2
else:
    barato = produto3


print(f'Você deve comprar o produto que custa R$ {barato:.2f}.')