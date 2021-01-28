"""Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares 
e a quantidade de números impares."""

par = 0
imp = 0
for x in range(1, 11):
    n = int(input(f'Digite o {x}º número: '))
    if n % 2 == 0:
        par += 1
    else:
        imp += 1
print(f'Ao todo temos {par} números pares e {imp} números ímpares.')

