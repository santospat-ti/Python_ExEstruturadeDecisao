#Faça um Programa que leia um número e exiba o dia correspondente da semana. 
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

dia_sem = int(input('Digite um número de 1 a 7: '))

def verificadia(dia_sem):
    dicio_sem = {1: 'domingo', 2: 'segunda-feira', 3: 'terça-feira', 4: 'quarta-feira', 5: 'quinta-feira', 6: 'sexta-feira', 7: 'sábado'}

    for dia in dicio_sem.keys():
        if dia_sem == dia:
            print(dicio_sem[dia].capitalize())
            break
    else:
        print('Dia não encontrado.')

verificadia(dia_sem)

#PRAPOSTAR
