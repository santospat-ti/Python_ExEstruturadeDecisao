"""A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... 
Faça um programa que gere a série até que o valor seja maior que 500."""

ultimo = 1
penultimo = 1
count = 1
resul = 500

while count != resul:
    termo = ultimo + penultimo
    penultimo = ultimo
    ultimo = termo
    count += 1
    """for count in range(1, 500):
        print(count)
        break"""
print(termo, end=' ')