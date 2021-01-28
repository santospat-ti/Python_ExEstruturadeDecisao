"""Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do 
percentual do ano anterior. Faça um programa que determine o salário atual desse funcionário. 
Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário."""

sal_inicial = float(input('Digite o salário inicial R$ '))
aumento = 1.5

for i in range(1996, 2020 + 1):
    aumento = aumento * 2
    sal_atual = sal_inicial + (sal_inicial * (aumento / 100))
    print(f'Salário em {i} = {sal_atual}')