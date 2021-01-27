#Tendo como dado de entrada a altura (h) de uma pessoa, 
# construa um algoritmo que calcule seu peso ideal, 
# utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

h = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
sexo = str(input('Digite seu sexo: ')).strip().upper()
while sexo not in 'F/M':
    sexo = str(input('Digite seu sexo: [F/M] ')).strip().upper()

peso_ideal = (72.2*h) - 58 if sexo == 'M' else (62.1*h) - 44.7

if peso < peso_ideal:
    print('Abaixo do peso ideal.')
elif peso == peso_ideal:
    print('Dentro do peso ideal.')
else:
    print('Acima do peso ideal.')

print(f'Peso: {peso:.2f}. / Peso ideal {peso_ideal:.2f}')