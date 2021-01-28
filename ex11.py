#Altere o programa anterior para mostrar no final a soma dos números.

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

soma = 0
for x in range(n1, n2, 1):
    soma += x
print(soma)