"""Em uma competição de salto em distância cada atleta tem direito a cinco saltos. No final da série de saltos de cada atleta,
o melhor e o pior resultados são eliminados. O seu resultado fica sendo a média dos três valores restantes. 
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois 
informe a média dos saltos conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média). 
Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da execução, portanto não são ordenados. 
O programa deve ser encerrado quando não for informado o nome do atleta. 
A saída do programa deve ser conforme o exemplo abaixo:
Atleta: Rodrigo Curvêllo

Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Melhor salto:  6.5 m
Pior salto: 5.3 m
Média dos demais saltos: 5.9 m

Resultado final:
Rodrigo Curvêllo: 5.9 m"""

atletas = True
n_atleta = 1
while atletas != '':
    saltos = []
    print('\n' * 5)
    print('Atleta nº', n_atleta)
    atletas = input('Digite o nome do atleta: ')
    if atletas == '':
        break
    else:
        n_saltos = 1
        print('\n' * 3)
        for s in range(5):
            print('Salto nº', n_saltos)
            distanc_salto = float(input(f'Digite a distância em metros do {s + 1}º salto: '))
            saltos.append(distanc_salto)
            n_saltos += 1
        print('Atleta: ', atletas)
        n_saltos = 1
        count = 0
        for i in range(5):
            print(n_saltos, 'º salto :', saltos[count], 'm')
            n_saltos +=1
        print('Melhor salto: ', max(saltos), ' m')
        print('Pior salto: ', min(saltos), ' m')

        saltos.remove(max(saltos))
        saltos.remove(min(saltos))
        media = sum(saltos) / len(saltos)
        print('Média dos demais saltos: ', round(media, 2))
        print('Resultado final: \n', atletas, ' : ', round(media, 2))
        n_atleta += 1