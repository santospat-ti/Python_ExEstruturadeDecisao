"""Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool: até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina: até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, 
o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a 
ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90."""

def combustíveis():

    combustível = {2.50 : "G-Gasolina",
                   1.90 : "A-Álcool"}

    valorG = 2.50
    valorA = 1.90

    
    
    comb = str(input('G-gasolina\nA-Álcool ')).upper()
    if comb in "AG":    
        litros = float(input('Litros: '))
       
        if litros.__float__() <= 20 and comb == "A":       
            desc = valorA * litros - (litros * 0.3)
            print(f'Com {litros:.2f} litros de álcool o valor a ser pago é R$ {desc:.2f}.')

        elif litros.__float__() > 20 and comb == "A":
            desc = valorA * litros - (litros * 0.5)
            print(f'Com {litros:.2f} litros de álcool o valor a ser pago é R$ {desc:.2f}.')

        elif litros.__float__() <= 20 and comb == "G":
            desc = valorG * litros - (litros * 0.4)
            print(f'Com {litros:.2f} litros de gasolina o valor a ser pago é R$ {desc:.2f}')

        elif litros.__float__() > 20 and comb == "G":
            desc = valorG * litros - (litros * 0.6)
            print(f'Com {litros:.2f} litros de gasolina o valor a ser pago é R$ {desc:.2f}')

combustíveis()

    