#Faça um programa que leia 5 números e informe o maior número.

lista = []
for x in range(5):
    lista.append(int(input('Informe um número: ')))
print(max(lista))