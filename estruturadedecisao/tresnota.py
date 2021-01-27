"""Faça um Programa para leitura de três notas parciais de um aluno. 
O programa deve calcular a média alcançada por aluno e presentar:
A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
A mensagem "Aprovado com Distinção", se a média for igual a 10."""

def entraNota(quantidade_nota):
    notas = []
    int = 1
    for num in range(quantidade_nota):
        nota = (float(input("Digite a {0}ª nota: ".format(int))))
        if nota < 0 or nota > 10:
            raise ValueError('Erro na {0}ª nota. Digite uma nota entre 0 e 10.'.format(int))
        notas.append(nota)
        int += 1
        
    return notas

def mediaAluno(notas):
    soma = sum(notas)
    print(soma)
    media = soma/len(notas)
    
    if media > 7.0 and media < 10:
        print('Aprovado com média: {0}'.format(media))
    
    elif media < 7.0:
        print('Reprovado com média: {0}'.format(media))
    
    else:
        print('Aprovado com distinção: 10!')


notas = entraNota(3)
mediaAluno(notas)