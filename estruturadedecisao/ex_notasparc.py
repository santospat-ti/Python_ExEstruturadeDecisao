""""Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, 
e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem APROVADO 
se o conceito for A, B ou C ou REPROVADO se o conceito for D ou E."""

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2

print('''Entre 9.0 e 10.0   A 
Entre 7.5 e 9.0   B
Entre 6.0 e 7.5 C
Entre 4.0 e 6.0 D
Entre 4.0 e zero E''')

if media > 9 and media <= 10:
    print(f'Suas notas foram {nota1:.2f} e {nota2:.2f}.')
    print('O aluno tirou A e foi Aprovado!')

elif media >= 7.5 and media < 9:
    print(f'Suas notas foram {nota1:.2f} e {nota2:.2f}.')
    print('O aluno tirou B e foi Aprovado!')

elif media >= 6.5 and media < 7.5:
    print(f'Suas notas foram {nota1:.2f} e {nota2:.2f}.')
    print('O aluno tirou C e foi Aprovado!')

elif media >= 4 and media < 6:
    print(f'Suas notas foram {nota1:.2f} e {nota2:.2f}.')    
    print('O aluno tirou D e foi Reprovado!')

elif media < 4:
    print(f'Suas notas foram {nota1:.2f} e {nota2:.2f}.')
    print('O aluno tirou E e foi Reprovado!')

else:
    print('Nota inválida!')