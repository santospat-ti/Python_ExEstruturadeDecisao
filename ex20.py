"""Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes 
e limitando o fatorial a números inteiros positivos e menores que 16."""

import math
lista = []
c = 0

quant = int(input('Digite a quantidade de números que deseja fatorar: '))
while quant != c:
    n = float(input('Digite um número entre 0 e 16. '))

    while n // 1 != n or n < 0 or 0 or n < 16:
        n = float(input('ERRO! Digite um número válido.'))

    

    print(f'Fatorial do número digitado: {math.factorial(n)}')
    c += 1