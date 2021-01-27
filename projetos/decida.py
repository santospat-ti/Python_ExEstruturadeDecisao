import random
from time import sleep
respostas = ['Sim, vai lá!',
             'Larga mão!',
             'Você quem sabe!',
             'Hahahaha não brinca!',
             'Acho melhor você não ir',
             'Se eu fosse tu, eu iria!',
             'Xiii, rapaz. Sei não hein.',
             'Claro, com certeza!',
             'Adoraria ver isso!',
             'O quê?! Em plena pandemia?!',
             'Não sei se elx tá muito afim',
             'Já fui lá, é bom!']
while True: 
    pergunta = input('Digite sua pergunta: ')
    print('Pensando no melhor conselho...')
    sleep(1)
    print(random.choice(respostas))
    pergunta_2 = input('Deseja outro conselho: [S/N]').upper()
    while pergunta_2 not in 'SsNn':
        pergunta_2 = input('Digite Sim ou Não: ').upper()
    if pergunta_2 == 'N':
        break