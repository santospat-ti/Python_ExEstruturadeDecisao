"""Faça um Programa que pergunte em que turno você estuda. 
Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
Imprima a mensagem Bom Dia!, Boa Tarde! ou Boa Noite! ou Valor Inválido!, conforme o caso."""

turno = str(input(f'Em que turno você estuda?\n'
 '\t[M=Matutino]\n'
 '\t[V=Vespertino]\n'
 '\t[N=Noturno]\n')).upper().strip()

if turno == 'M':
    print(f'Bom dia!')
elif turno == 'V':
    print(f'Boa tarde!')
elif turno == 'N':
    print(f'Boa noite!')
else: 
    print('Valor inválido!')