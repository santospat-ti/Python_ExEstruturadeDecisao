#Faça um Programa para uma loja de tintas. O programa 
# deverá pedir o tamanho em metros quadrados da área 
# a ser pintada. Considere que a cobertura da tinta é 
# de 1 litro para cada 6 metros quadrados e que a 
# tinta é vendida em latas de 18 litros, que custam 
# R$ 80,00 ou em galões de 3,6 litros, que custam 
# R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem 
# compradas e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o desperdício 
# de tinta seja menor. Acrescente 10% de folga e 
# sempre arredonde os valores para cima, isto é, 
# considere latas cheias.

print('='*3, 'CASA DAS TINTAS', '='*3)
a = float(input('Digite o tamanho da área a ser pintada: '))
litros = a / 6
latas = litros // 18 + 1
galões = litros // 3.6 + 1
preço_latas = latas * 80
preço_galões = galões * 25
combinação = (litros//18)*80+((litros%18)//3.6+1*25)

print(f'O preço com latas é {preço_latas}')
print(f'O preço com galões é {preço_galões}')
print(f'O preço com combinações é {combinação}')