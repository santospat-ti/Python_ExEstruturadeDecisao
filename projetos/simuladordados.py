from random import randint
from time import sleep

dados = randint(1, 6)
dado = input('Você gostaria de jogar o dado? [S/N] ').upper()
if dado == '' or dado == ' ':
    print('ERRO. Por favor, digite S para Sim e N para NãO.')
    dado = input('Digite [S/N] ').upper()
    if dado == 'N':
        print('Até a próxima.')
       
    else:
        print('Sorteando...')
        sleep(2)
        print('Você tirou', dados,' no dado.')