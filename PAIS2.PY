"""Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. 
Valide a entrada e permita repetir a operação."""

população_a = float(input('Informe o número de habitantes da cidade A: '))
população_b = float(input('Informe o número de habitantes da cidade B: '))
atax = float(input('Taxa de crescimento inicial da cidade A: % '))
btax = float(input('Taxa de crescimento inicial da cidade B: % '))

ano = 0
while população_a <= população_b:
    população_a += round((população_a * atax) / 100)
    população_b += round((população_b * btax) / 100)
    ano = ano + 1

print(f'Levará {ano} anos para a população de A ser maior que B.')
print(f"{população_a:.2f} e {população_b:.2f}")