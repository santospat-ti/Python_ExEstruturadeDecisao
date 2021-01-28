"""O cardápio de uma lanchonete é o seguinte:
Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00
Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. 
Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. 
Considere que o cliente deve informar quando o pedido deve ser encerrado."""

codigos = [100, 101, 102, 103, 104, 105]
alimento_ = ['Cachorro Quente', 'Bauru Simples', 'Bauru com ovo', 
            'Hambúrger', 'Cheeseburguer', 'Refrigerante']
preco_ = [1.20, 1.30, 1.50, 1.20, 1.30, 1.00]
pedidos_lista = []
n_pedido = 1
codigo_pedido = True

while codigo_pedido != 0:
    print('\nPedido nº', n_pedido)
    codigo_pedido = int(input('Digite o código do pedido: '))
    if codigo_pedido == 0:
        break
    else:
        while codigo_pedido not in codigos:
            print(f'Código não registrado. ')
            codigo_pedido = int(input('Digite o código do pedido: '))
            indice = codigos.index(codigo_pedido)
        quantidade = int(input('Digite a quantidade desejada: '))
        valor_pedido = preco_[indice] * quantidade
        pedidos_lista.append(valor_pedido)
        n_pedido += 1

pedido_nota = 0
print('\n' * 2)

for pedido in range(n_pedido - 1):
    print('Pedido nº ', pedido_nota + 1, ' R$ ', round(pedidos_lista[pedido_nota], 2))
    pedido_nota += 1
print('Total: R$', round(sum(pedidos_lista), 2))