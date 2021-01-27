#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

alfa = str(input('Digite uma letra: ')).strip().upper()

if alfa.isalpha():
    if alfa == "A" or alfa == "E" or alfa == "I" or alfa == "O" or alfa == "U":
        print('Você digitou uma vogal.')
    else:
        print('Você digitou uma consoante.')
else:
    print('Não é uma letra!')
