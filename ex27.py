"""Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a 
quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos."""

quant_turma = int(input('Qual a quantidade de turmas? '))
alunos_turma = []
turma = 1


for aluno in range(quant_turma):
    print(f'{turma}')
    alunos = int(input('Alunos da turma: '))
    while alunos > 40:
        print(f'{turma}! Uma turma só pode ter 40 alunos.')
        alunos = int(input('Alunos da turma: '))
    turma += 1
    alunos_turma.append(alunos)

media = sum(alunos_turma) / len(alunos_turma)
print(f'A média é igual a {media:.2f}.')