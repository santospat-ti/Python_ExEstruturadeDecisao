"""Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores."""

lista = []
for i in range(6):
    lista.append(int(input(f'Digite o {i}º número: ')))
print(lista)
print(f'O maior valor é {max(lista)}.')
print(f'O menor valor é {min(lista)}.')
print(f'A soma dos valores é {sum(lista)}.')
