"""Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. 
Um número primo é aquele que é divisível somente por ele mesmo e por 1."""


n = int(input('Digite um número: '))
mult = 0

for p in range(2, n):
    if n % p == 0:
        mult += 1
        print(f'Múltiplo de {p}')
if (mult == 0):
    print('É primo.')
else:
    print(f'Tem {mult} múltiplos acima de 2 e abaixo de {n}.')
