#Faça um programa que calcule o mostre a média aritmética de N notas.
 


quant_notas = int(input('Digite a quantidade de notas que deseja: '))
count = 0
lista_notas = []

while count < quant_notas:
    notas = lista_notas.append(float(input('Digite as notas: ')))
    count += 1

media = sum(lista_notas) / quant_notas 
print(f'A média de notas é {media:.2f})

