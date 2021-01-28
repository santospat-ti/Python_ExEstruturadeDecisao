"""Foi feita uma estatística em 5 cidades brasileiras para coletar dados sobre acidentes de trânsito. 
Foram obtidos os seguintes dados:
Código da cidade;
Número de veículos de passeio (em 1999);
Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
Qual a média de veículos nas cinco cidades juntas;
Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio."""


código_cidades = []
n_veiculos = []
n_acidentes = []
acidentesvei_2000 = []

for c in range(5):
    código = int(input('Digite o código da cidade: '))
    while código in código_cidades:
        código = int(input('Código cadastrado. Digite o código de outra cidade: '))

    numero_veiculos = int(input('Número de veículos de passeio (em 1999): '))
    numero_acidentes = int(input('Número de acidentes de trânsito com vítimas: '))

    if numero_veiculos > 2000:
        acidentesvei_2000.append(numero_acidentes)
        n_acidentes.append(numero_acidentes)
    else:
        n_acidentes.append(numero_acidentes)

    n_veiculos.append(numero_veiculos)
    código_cidades.append(código)

maior_acidentes_id = n_acidentes.index(max(n_acidentes))
menor_acidentes_id = n_acidentes.index(min(n_acidentes))
print("\n" * 3)
print(f'O maior índice de acidentes de trânsito é {max(n_acidentes)}\n Código da cidade: {código_cidades[maior_acidentes_id]}.')
print(f'O menor índice de acidentes de trânsito é {min(n_acidentes)}\n Código da cidade: {código_cidades[menor_acidentes_id]}.')
print()

media_veiculos = sum(n_veiculos) / len(n_veiculos)
print("\nMédia de veículos nas 5 cidades: ", media_veiculos)

print("\n" * 2)
média_acidentes_2000 = sum(acidentesvei_2000) / len(acidentesvei_2000)
print(f'Média de acidentes com menos de 2000 veículos {média_acidentes_2000:.2f}.')