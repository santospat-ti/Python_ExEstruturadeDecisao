"""Faça um Programa que peça um número e informe se o número é inteiro ou decimal. 
Dica: utilize uma função de arredondamento."""

num = float(input('Digite um número: '))

if num == round(num):
    print('Inteiro')
else:
    print('Decimal')
    print(f'Arrendodado pra cima, {round(num + 0.5)}')
    print(f'Arredondado pra baixo: {round(num - 0.5)}')
    print(f'{round(num, 1)}')

    