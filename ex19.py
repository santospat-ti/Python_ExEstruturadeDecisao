"""Altere o programa anterior para que ele aceite apenas números entre 0 e 1000."""


lista = []
c = 0

quant = int(input('Digite a quantidade de números que deseja: '))
while quant != c:
    n = float(input('Digite um número entre 0 e 1000. '))

    while n > 1000 or n < 0:
        n = float(input('ERRO! Digite um número válido: '))
    lista.append(n)    
    c += 1

print(f'O maior valor é {max(lista)}, o menor {min(lista)} e a soma {sum(lista)}.')