"""O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas. 
Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu um tabela que contém 
o número de itens que o cliente comprou e ao lado o valor da conta. Desta forma a atendente do caixa 
precisa apenas contar quantos itens o cliente está levando e olhar na tabela de preços. Você foi contratado 
para desenvolver o programa que monta esta tabela de preços, que conterá os preços de 1 até 50 produtos, 
conforme o exemplo abaixo:
Lojas Quase Dois - Tabela de preços
1 - R$ 1.99
2 - R$ 3.98
...
50 - R$ 99.50"""

quant_prod = int(input('Digite a quantidade de produtos: '))
while quant_prod > 50:
    quant_prod = int(input('Digite a quantidade de produtos [menos de 50]: '))

preços = []
n_produto = 1
cont  = 0

for x in range(quant_prod):
    preços.append(float(input(f'Digite o preço do produto {x} R$: ')))
    n_produto += 1

print('Lojas Quase Dois - Tabela de Preços')
n_produto = 1
for y in range(quant_prod):
    print(f'Produto Nº {n_produto} - R$ {preços[cont]}')
    cont += 1
    n_produto += 1
