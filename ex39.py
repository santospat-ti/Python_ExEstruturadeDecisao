"""Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo 
representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. 
Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas."""

aluno_n = []
aluno_a = []
cont = 1



for p in range(10):
    print("\nDigitação número", p + 1," :")
    número = int(input('Digite o número do aluno: '))
    while número in aluno_n:
        print('Este número já foi digitado.')
        número = int(input('Digite outro número: '))
    altura = float(input('Digite a altura do aluno: '))
    aluno_n.append(número)
    aluno_a.append(altura)
    cont += 1

id_alto = aluno_a.index(max(aluno_a))
id_baixo = aluno_a.index(min(aluno_a))


print(f'\nO aluno mais é baixo é: {aluno_n[id_baixo]}\n e tem {min(aluno_a):.1f}.')
print(f'\nO aluno mais alto é: {aluno_n[id_alto]}\n e tem {max(aluno_a):.1f}.')
