#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês.

salario = float(input('Quanto você ganha por hora? '))
total = float(input('Qual o número de horas trabalhadas no mês? '))
resultado = salario * total
print(f'O total do seu salário é', resultado)