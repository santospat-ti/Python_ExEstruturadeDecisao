"""Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto 
em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um."""

quant_cd = int(input('Quantos CDs você possui? '))
cd_colecao_preços = []
n_cds = 1

for cd in range(quant_cd):
    cds_preço = float(input(f'Qual o valor do {cd}º: '))
    n_cds += 1
    cd_colecao_preços.append(cds_preço)

media = sum(cd_colecao_preços) / len(cd_colecao_preços)
print(f'O valor médio gasto é R$ {media:.2f}')
