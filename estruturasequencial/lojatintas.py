#Faça um programa para uma loja de tintas. 
# O programa deverá pedir o tamanho em metros 
# quadrados da área a ser pintada. Considere que a 
# cobertura da tinta é de 1 litro para cada 3 metros 
# quadrados e que a tinta é vendida em latas de 
# 18 litros, que custam R$ 80,00. 
# Informe ao usuário a quantidades de latas de tinta 
# a serem compradas e o preço total.

print('='*3, 'Loja de Tintas', '=' * 3)
a = int(input('Valor em metros da área: '))
litros = a / 3
preço = 80.0
capacidadeL = 18
latas = litros / capacidadeL
total = latas * preço
print(f'Serão {latas:.2f} latas de tinta.')
print(f'E o valor será de R$ {total:.2f}.')