"""Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de 
idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, 
conforme a média calculada."""

quant_pessoas = int(input("Digite o número de pessoas que você irá digitar: "))
todas_idades = []

for id in range(quant_pessoas):
    idade = todas_idades.append(int(input("Digite as idades: ")))

#cálculo para saber a média e mostrar um dos resultados 
if sum(todas_idades) / len(todas_idades) < 25:
    print('Jovem')
elif sum(todas_idades) / len(todas_idades) >= 25 and sum(todas_idades) / len(todas_idades) < 60:
    print('Adulto') 
else:
    print('Idoso')