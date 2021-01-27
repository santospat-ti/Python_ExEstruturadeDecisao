#abre o arquivo para leitura
arquivoEntrada = open('22_entrada.txt', 'r')

#coloca todas as linhas em memoria
linhas = arquivoEntrada.readlines()

#fecha o arquivo
arquivoEntrada.close()

usuarios = []
espacosutilizados = []
espacototal = 0.0

for linha in linhas:
    campos = linha.split()
    usuario = campos[0]
    espacosutilizado = int(campos[1])
    usuarios.append(usuario)
    espacosutilizados.append(espacosutilizado)
    espacototal += espacosutilizado

#abre o arquivo para escrita
arquivoSaida = open('23_saida.txt', 'w')

arquivoSaida.write(
    'ACME Inc.             Uso do espaço em disco pelos usuários\n')
arquivoSaida.write('\nNr.   Usuário     Espaço Utilizado    %%    do uso')

for i in range(0, len(usuarios)):
    espacoMB = espacosutilizados[i] / (1024.0 * 1024.0)
    percentualUso = espacosutilizados[i] / espacototal
    arquivoSaida.write(f'\n {i + 1} - {usuarios[i]} - {espacoMB} - {percentualUso * 100.0}')

arquivoSaida.write(f'Espaço Total ocupado: {espacototal / (1024.0 * 1024.0)} MB')
arquivoSaida.write(f'Espaço médio ocupado: {espacototal / len(usuarios) / (1024.0 * 1024.0)}')

#fecha o arquivo
arquivoSaida.close()