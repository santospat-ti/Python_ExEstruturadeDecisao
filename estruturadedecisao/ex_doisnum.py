"""Faça um Programa que peça dois números e imprima o maior deles."""
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

if n1 > n2:
    print(f'{n1} é o maior número. ')
if n1 == n2:
    print(f'Os números são iguais.')
else:
    print(f'{n2} é o maior número.')