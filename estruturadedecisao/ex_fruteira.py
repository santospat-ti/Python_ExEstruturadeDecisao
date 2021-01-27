"""Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar 
R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo 
para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas 
e escreva o valor a ser pago pelo cliente."""

print('\tFRUTEIRA DO JOSÉ RICARDO')


def calcular_precos():

    #variavel
    count = 0
    calculo_produto = 0

    #dados do produto
    dados_produto = [("morango", 2.50, 2.20), ("maçã", 1.80, 1.50)]

    while True:

        #variavel
        finalizar = False
        #perguntar qual tipo de produto desejado.
        produto = input("Por favor, informe o produto desejado (Morango ou Maçã): ")

        for x in range(2):
            #verificar se tem o produto desejado
            if produto.lower() == dados_produto[x][0]:
                #armazenar a posição do produto na variável count
                count = x
                #inserir o valor booleano true para a variável, interrompendo o loop while
                finalizar = True
                #interromper o loop for caso tenha encontrado o determinado produto
                break

            else:
                if x == 1:
                    #informa que o valor está inválido
                    finalizar = False 
                    print("Valor inválido.", produto)
        if finalizar:
            break

    while True:

        try:

            #obter o peso do produto
            peso = float(input("Por favor, informe o peso desejado."))

            #verifica se o peso está acima de zero
            if peso > 0:
                break
            else:
                continue

        except ValueError:
            print("Valor inválido do peso.")
            continue

    #calculos do produto
    if peso <= 5 and peso > 0:
        #calculando o valor do produto com o peso
        calculo_produto = dados_produto[count][1] * peso
    elif peso > 5:
        #calculando o valor do produto com o peso.
        calculo_produto = dados_produto[count][2] * peso
        #verificando se o peso é maior que 8kg ou o valor maior que R# 25
        if peso > 8 or calculo_produto > 25:
            calculo_produto = (dados_produto[count][2] * peso - ((dados_produto[count][2] * peso) * 10 / 100))

    print(f"Valor a pagar: R${calculo_produto:.2f}.")

calcular_precos()

