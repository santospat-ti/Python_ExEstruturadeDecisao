"""Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. 
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato."""

total_eleit = int(input('Qual o número total de eleitores: '))

votos = []
cont = 0

for eleitos in range(total_eleit):
    votos.append(int(input('Digite seu voto \n[1]\n[2]\n[3]:')))
    cont += 1

print(f'Votos para candidadato 1: {votos.count(1)}')
print(f'Votos para candidadato 2: {votos.count(2)}')
print(f'Votos para candidadato 3: {votos.count(3)}')