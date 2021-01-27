#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo .
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo.

n1 = int(input('1º número inteiro: '))
n2 = int(input('2º número inteiro: '))
n3 = float(input('Digite um número real: '))

print(f'Produto: {n1*2*n2/2}')
print(f'Soma: {(3*n1)+n3}')
print(f'Cubo: {n3**3}')
