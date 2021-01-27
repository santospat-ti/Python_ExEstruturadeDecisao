"""O Hipermercado Tabajara está com uma promoção de 
carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites 
para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% 
sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom 
fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e 
valor a pagar."""

import sys
print()
print("\tBem-vindo ao Hipermercado Tabajara")
print("\tEscolha o tipo de carne que quer levar: \n")

tipo_carne = input("\tF-Filé Duplo \n\tA-Alcatra \n\tP-Picanha: ")
peso = float(input("\tDigite o peso desejado: "))
if float(peso) <= 5.0:
    preço_filé = 4.90
    preço_alcatra = 5.90
    preço_picanha = 6.90
else:
    preço_filé = 5.80
    preço_alcatra = 6.80
    preço_picanha = 7.80

if tipo_carne.lower() == 'f':
    valor = preço_filé * peso
    tipo_carne = 'Filé Duplo'     
elif tipo_carne.lower() == 'a':
    valor = preço_alcatra * peso
    tipo_carne = 'Alcatra'
elif tipo_carne.lower() == 'p':
    valor = preço_picanha * peso
    tipo_carne = 'Picanha'
else: 
    print('\tEscolha errada!')
    sys.exit


pag = input("\tDeseja pagar com Cartão Tabajara: \n\t[S]im / [N]ão")
valordesc = valor * 0.05
if pag.lower() == "s":
    preço_final = valor - valordesc
else:
    preço_final = valor

print(f"\tTipo: {tipo_carne}\n\tPeso: {peso}\n\tValor: {valor}")
if preço_final != valor:
    print(f'\tDesconto de 5%: R$ {valordesc:.2f}')
    print(f'\tPreço final R$ {preço_final:.2f}')
else:
    print(f'\t Preço final R$ {preço_final}')