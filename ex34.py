"""Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. 
Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça 
um número inteiro e determine se ele é ou não um número primo."""

n = int(input('Digite um número: '))

if n % 2 == 0 and n != 2:
    print('Não é primo.')
else:
    print('É primo.')