"""Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, 
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, 
mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. 
No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00"""

print(f'\tFOLHA DE PAGAMENTO')
valor_hora = float(input('Valor da hora: R$ '))
horas_m = float(input('Horas trabalhadas no mês: '))
salario = valor_hora * horas_m


ir = ''
inss = (10 / 100 * salario)
descontoinss = inss - salario 
fgts = (11 / 100 * salario)
descontof = fgts - salario 
total = ''

if salario <= 900:
    ir = ''
    print(f'\tSalário Bruto: R$ {salario}')
    print(f'\t(-) IR - isento')
    print(f'\t(-) INSS (10%) : R$ {inss}')
    print(f'\t(-) FGTS (11%) : R$ {fgts}')
    print(f'\tTotal de descontos : R$ {inss}')
    print(f'\tSalário líquido : R$ {salario - inss}')

elif salario <= 1500:
    ir = (5 / 100) * salario
    desconto = ir - salario
    total = ir + inss
    print(f'\tSalário Bruto: : R$ {salario}')
    print(f'\t(-) IR (5%) : R$ {ir}')
    print(f'\t(-) INSS (10%) : R$ {inss}')
    print(f'\t(-) FGTS (11%) : R$ {fgts}')
    print(f'\tTotal de descontos : R${total}')
    print(f'\tSalário Líquido : R${salario - inss - ir}')



elif salario <= 2500:
    ir = (10 / 100) * salario
    desconto = salario - ir
    total = ir + inss 
    print(f'\tSalário Bruto: 5 * {horas_m} : R$ {salario}')
    print(f'\t(-) IR (5%) : R$ {ir}')
    print(f'\t(-) INSS (10%) : R$ {inss}')
    print(f'\t(-) FGTS (11%) : R$ {fgts}')
    print(f'\tTotal de descontos : R${total}')
    print(f'\tSalário Líquido : R${salario - inss - ir}')

elif salario > 2500:
    ir = (20 / 100) * salario
    desconto = salario - ir 
    total = ir + inss
    print(f'\tSalário Bruto: 5 * {horas_m} : R$ {salario}')
    print(f'\t(-) IR (5%) : R$ {ir}')
    print(f'\t(-) INSS (10%) : R$ {inss}')
    print(f'\t(-) FGTS (11%) : R$ {fgts}')
    print(f'\tTotal de descontos : R${total}')
    print(f'\tSalário Líquido : R${salario - inss - ir}')

