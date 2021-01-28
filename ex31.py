"""O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. 
Faça um programa que implemente uma caixa registradora rudimentar. 
O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. 
Um valor zero deve ser informado pelo operador para indicar o final da compra. O programa deve então mostrar
 o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. 
 Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser conforme 
 o exemplo abaixo:
Lojas Tabajara 
Produto 1: R$ 2.20
Produto 2: R$ 5.80
Produto 3: R$ 0
Total: R$ 9.00
Dinheiro: R$ 20.00
Troco: R$ 11.00
..."""
import time

while True: 
    preços_produtos = []
    preço_produto = True
    n_produto = 1

    while preço_produto != 0:
        print(f'Produto {n_produto}')
        preço_produto = float(input('Digite o valor do produto R$ '))
        preços_produtos.append(preço_produto)
        n_produto += 1


    print(f'Total: {sum(preços_produtos)}')
    dinheiro = float(input('Digite a quantia que irá pagar: '))

    while dinheiro < sum(preços_produtos):
        dinheiro = float(input('Digite a quantia de que irá pagar: R$ '))

    print(f'Dinheiro: R$ {dinheiro:.2f}')
    print(f'Troco: R$ {dinheiro - sum(preços_produtos)}')
    print('Próxima compra em 3 segundos...')
    time.sleep(3)
    print("\n" * 5)