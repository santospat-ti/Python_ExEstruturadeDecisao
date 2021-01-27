"""Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido."""

sexo = str(input('Digite seu sexo: ')).strip()[0].upper()
if sexo not in 'FM':
    print(f'Sexo inválido. Digite M ou F.')
elif sexo == 'F':
    print(f'F - Feminino')
else:
    print(f'M - Masculino')
        