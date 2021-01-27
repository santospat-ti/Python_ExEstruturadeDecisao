print(f'\tFOLHA DE PAGAMENTO')
valor_h = float(input('Valor da hora: R$ '))
horas_m = float(input('Horas trabalhadas no mês: '))
salario_bruto = valor_h * horas_m

def desconto(salario_bruto):
    ir = 0
    sindicato = (salario_bruto/100)*3
    fgts = (salario_bruto/100)*11
    inss = (salario_bruto/100)*10

    if salario_bruto <= 900:
        salario_liq = salario_bruto - sindicato

    elif salario_bruto <= 1500:
        ir = (salario_bruto/100)*5
        salario_liq = salario_bruto - sindicato - fgts - inss

    elif salario_bruto <= 2500:
        ir = (salario_bruto/100)*10
        salario_liq = salario_bruto - sindicato - fgts - inss

    elif salario_bruto > 2500:
        ir = (salario_bruto/100)*20
        salario_liq = salario_bruto - sindicato - fgts - inss
    
    imprime(salario_bruto, ir, inss, fgts, salario_liq)

def imprime(salario_bruto, ir, inss, fgts, salario_liq):
    print(f'''
    Salário Bruto : R${salario_bruto}
    (-) IR (5%) : R${ir}
    (-) INSS (10%) : R${inss}
    (-) FGTS (11%) : R${fgts}
    Salário Líquido : R${salario_liq}''')

desconto(salario_bruto)




