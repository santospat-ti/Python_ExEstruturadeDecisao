#Tendo como dados de entrada a altura de uma pessoa, 
# construa um algoritmo que calcule seu peso ideal, 
# usando a seguinte fórmula: (72.7*altura) - 58

altura = float(input('Digite sua altura: '))
vt = 72.7*altura
peso = vt - 58
print(f'Seu peso ideal é {peso}')