"""Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, 
a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes 
da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário 
digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados os códigos e valores do 
clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes"""


codigo_c = []
altura_c = []
peso_c = []
n_usuario = 1
codigo_usuario = True


while codigo_usuario != 0:
    print("\nCliente nº", n_usuario)
    codigo_usuario = int(input('Digite seu código: '))
    if codigo_usuario == 0:
        break
    else:
        altura = float(input('Digite sua altura: '))
        peso = float(input('Digite seu peso: '))
        codigo_c.append(codigo_usuario)
        altura_c.append(altura)
        peso_c.append(peso)
        n_usuario += 1



cod_alto = altura_c.index(max(altura_c))
cod_baixo = altura_c.index(min(altura_c))
cod_magro = peso_c.index(min(peso_c))
cod_gordo = peso_c.index(max(peso_c))
print('\n' * 3)
print(f'Código do mais alto: ', codigo_c[cod_alto])
print(f'Código do mais baixo: ', codigo_c[cod_baixo])
print(f'Código do mais magro: ', codigo_c[cod_magro])
print(f'Código do mais gordo: ', codigo_c[cod_gordo])
print()
print(f'A média de altura é {round(sum(altura_c) / len(altura_c))} metros.')
print(f'A média de peso é {sum(peso_c) / len(peso_c)} kg.')