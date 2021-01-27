"""Faça um Programa que peça um número inteiro e determine se ele é par ou impar. 
Dica: utilize o operador módulo (resto da divisão)."""

num = int(input('Digite um número: '))

if num % 2 == 0:
    print('par')
else:
    print('ímpar')

"""Já dissemos, em algum tutorial anterior, que 1 equivale ao True e 0 ao False.
Quando fazemos o resto da divisão por 2, o resultado é sempre 0 ou 1.

Então nosso código poderia ser assim:"""

    numero = int(input('Digite um inteiro: '))

    if numero%2 :
        print("Ímpar")
    else:
        print("Par")