"""Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal."""

n1 = float(input('Número 1: '))
n2 = float(input('Número 2: '))
op = str(input('Qual operação deseja realizar: (+, -, *, /): '))

if op == '+':
    resultado = n1 + n2
    if resultado % 2 == 0:
        print(f'O resultado {resultado:.2f} é par.')
    else:
        print(f'O resultado {resultado:.2f} é ímpar')
    if resultado >= 0:
        print(f'O resultado {resultado:.2f} é positivo')
    else:
        print(f'O resultado {resultado:.2f} é negativo')
    if resultado == round(resultado):
        print(f'O resultado {resultado:.2f} é inteiro')
    else:
        print(f'O resultado {resultado:.2f} é decimal')
if op == '-':
    resultado = n1 - n2
    if resultado % 2 == 0:
        print(f'O resultado {resultado:.2f} é par.')
    else:
        print(f'O resultado {resultado:.2f} é ímpar.')
    if resultado >= 0:
        print(f'O resultado {resultado:.2f} é positivo.')
    else:
        print(f'O resultado {resultado:.2f} é negativo.')
    if resultado == round(resultado):
        print(f'O resultado {resultado:.2f} é inteiro.')
    else:
        print(f'O resultado {resultado:.2f} é decimal.')
if op == '*':
    resultado = n1 * n2
    if resultado % 2 == 0:
        print(f'O resultado {resultado:.2f} é par.')
    else: 
        print(f'O resultado {resultado:.2f} é ímpar.')
    if resultado >= 0:
        print(f'O resultado {resultado:.2f} é positivo.')
    else:
        print(f'O resultado {resultado:.2f} é negativo.')
    if resultado == round(resultado):
        print(f'O resultado {resultado:.2f} é inteiro.')
    else:
        print(f'O resultado {resultado:.2f} é decimal.')
if op == '/':
    resultado = n1 / n2
    if resultado % 2 == 0:
        print(f'O resultado {resultado:.2f} é par.')
    else:
        print(f'O resultado {resultado:.2f} é ímpar.')
    if resultado >= 0:
        print(f'O resultado {resultado:.2f} é positivo.')
    else:
        print(f'O resultado {resultado:.2f} é negativo.')
    if resultado == round(resultado):
        print(f'O resultado {resultado:.2f} é inteiro.')
    else:
        print(f'O resultado {resultado:.2f} é decimal.')
       
      
