"""Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. 
O usuário deve informar de qual numero ele deseja ver a tabuada. """

n1 = int(input('Digite um número: '))
for x in range(0, 11):
    print(f'{n1} x {x} = {n1*x}')