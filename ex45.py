gabarito = []
respostas_aluno = []
notas_tiradas = []

print('\nProfessor: ')
for i in range(10):
    print('Questão: ', i + 1)
    resposta_certa = gabarito.append('Digite a resposta certa:')
n_aluno = 1
continuar = True

while continuar != 'n':
    print('\n' * 5)
    print('Aluno nº', n_aluno, ': ')
    respostas_aluno.clear()
    for i in range(10):
        print('Questão: ', i + 1)
        resposta_aluno = respostas_aluno.append(input('Digite a alternativa correta: '))
    nota = 0
    for i in range(10):
        if respostas_aluno[i] == gabarito[i]:
            nota += 1
        notas_tiradas.append(nota)
        continuar = input('Outro aluno vai utilizar o sistema: [s/n] ')
        n_aluno += 1

print(len(notas_tiradas), "alunos utilizaram o sistema.")
print('\nA maior nota tirada foi', max(notas_tiradas))
print('\nA menor nota tirada foi', min(notas_tiradas))
print('\nA média é', sum(notas_tiradas) / len(notas_tiradas))
print(notas_tiradas)

