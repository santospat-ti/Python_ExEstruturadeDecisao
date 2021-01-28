"""O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto 
indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média 
das temperaturas."""

import time

quant_temp = int(input("Quantidade de temperaturas que irá digitar: "))
temperaturas = []
n_temperatura = 1

for t in range(quant_temp):
    valor_temp = float(input('Digite os graus: '))
    temperaturas.append(valor_temp)
    n_temperatura += 1

m = round(sum(temperaturas) / len(temperaturas))
print(f'A menor temperatura informada é {min(temperaturas)}')
print(f'A maior temperatura informada é {max(temperaturas)}.')
print(f'A média de graus é {m}')