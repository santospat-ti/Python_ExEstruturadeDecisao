"""Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. 
Não utilize a função de potência da linguagem."""

base = int(input('Digite a base: '))
expoente = int(input('Digite o expoente: '))

#resultado
potencia = 1

for count in range(expoente):
    potencia *= expoente
    count += 1
print(f'{base} ^ {expoente} = {potencia}')