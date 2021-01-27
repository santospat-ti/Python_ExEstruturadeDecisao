from random import randint
from time import sleep

valor = randint(1, 4)
tentativa = 0
chute = 0
print()
while chute != valor:
    chute = int(input('\nChute um número: '))
    tentativa += 1
    
    while chute < 1 or chute > 4:
        chute = int(input('Chute um valor entre 1 e 4.'))
        break

    if chute < valor:
        print('Você jogou baixo demais!')
        resp = input('Deseja continuar: S/N ').upper()
        while resp not in 'SN':
            resp = input('Digite S ou N ').upper()
        if resp == 'N':
            break

    elif chute > valor:
        print('Você jogou alto mais!')
        resp = input('Deseja continuar: S/N ').upper()
        while resp not in 'SN':
            resp = input('Digite S ou N ').upper()
        if resp == 'N':
            break

    else:
        print(f'\nAcertou!')
print('\nFinalizando...')
sleep(1)
print(f'\nAo todos foram feitas {tentativa} tentativas.')





