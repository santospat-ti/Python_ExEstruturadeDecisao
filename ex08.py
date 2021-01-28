#Faça um programa que leia 5 números e informe a soma e a média dos números.

lista = []
for x in range(5):
    lista.append(int(input('Digite um número: ')))
    soma = sum(lista)
    media = soma / len(lista)
print(f'A soma é {soma} e a média é {media}.')