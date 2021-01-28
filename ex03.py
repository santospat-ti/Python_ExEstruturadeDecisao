"""Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';"""

nome = input('Nome: ')
while (len(nome) <= 3):
    nome = input('Informe um nome válido.')

idade = int(input("Idade: "))
while (idade < 0 or idade > 150):
    idade = int(input("Informe uma idade válida: "))

salario = float(input("Salário: "))
while (salario <= 0):
    salario = float(input("Informe um valor válido: "))

sexo = input("Sexo: [F] ou [M] ")
while (sexo.lower() != 'f' and sexo.lower() != 'm'):
    sexo = input('Informe um valor válido F ou M: ')

esta_civ = str(input(" [S]olteiro \n [C]asado \n [V]iúvo \n [D]ivorciado.")).lower()
while (esta_civ != 's' and esta_civ != 'c' and esta_civ != 'v' and esta_civ != 'd'): 
    esta_civ = str(input('Por favor, digite a inicial do seu estado civil.'))
