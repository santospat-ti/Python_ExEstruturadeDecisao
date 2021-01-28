"""Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. 
A saída deve ser conforme o exemplo abaixo:
Fatorial de: 5
5! =  5 . 4 . 3 . 2 . 1 = 120"""

fat = int(input('Digite o fatorial: '))
c = fat
f = 1

print(f'Calculando {fat}! = ', end='')
while c > 0:
    print(c, end=' ')
    print('x ' if c > 1 else '= ', end='')
    f *= c
    c -= 1
print(f'{f}')