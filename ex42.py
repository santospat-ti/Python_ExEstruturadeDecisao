"""Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles 
estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar 
quando for lido um número negativo.
"""


n_25 = []
n_50 = []
n_75 = []
n_100 = []
cont = True

while cont > 0:
    número = int(input('Digite o número: '))
    if número < 0:
        break
    else:
        if número > 0 and número <= 25:
            n_25.append(número)
        elif  número <= 50 and número > 25:
            n_50.append(número)
        elif número <= 75 and número > 50:
            n_75.append(número)
        elif número <= 100 and número > 75:
            n_100.append(número)

print(f'\n[0-25] : ', len(n_25))
print(f'\n[26-50] : ', len(n_50))
print(f'\n[51-75] : ', len(n_75))
print(f'\n[76-100] : ', len(n_100))

