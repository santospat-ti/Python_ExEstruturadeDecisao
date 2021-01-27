#Faça um Programa que leia três números e mostre o maior e o menor deles.

primeiro = float(input('Digite o primeiro número: '))
segundo = float(input('Digite o segundo número: '))
terceiro = float(input('Digite o terceiro número: '))

maior = primeiro
menor = primeiro

if segundo > maior:
    maior = segundo
if segundo < menor:
    menor = segundo
if terceiro > maior:
    maior = terceiro
if terceiro < menor:
    menor = terceiro
print(f'O maior número é {maior} e o menor é {menor}.')
