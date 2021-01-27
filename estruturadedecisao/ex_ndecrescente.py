#Faça um Programa que leia três números e mostre-os em ordem decrescente.

n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
n3 = float(input('Terceiro número: '))

if n1 < n3:
    n1, n3 = n3, n1
if n1 < n2:
    n1, n2 = n2, n1
if n2 < n3:
    n2, n3 = n3, n2

print(f'A ordem decrescente é {n1}, {n2} e {n3}')
