lista = []
qtd = 3
for i in range(qtd):
    elemento = int(input('Digite um número: '))
    lista.append(elemento)

lista.sort(reverse=True)
print(lista)