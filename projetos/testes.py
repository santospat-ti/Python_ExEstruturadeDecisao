votosAtletas =  [0]  * 23  
numeroAtleta = -1  
totalVotos = 0  
print 'Enquete: Quem foi o melhor jogador?'     
while (numeroAtleta  !=  0):
          numeroAtleta  = i nt (raw_input('Numero do jogador (0=fim): ' ))        if (numeroAtleta < 0) or (numeroAtleta > 23 ):          print 'Informe um valor entre 1 e 23 ou 0 para sair!' 
         continue        if (numeroAtleta != 0):          votosAtletas[numeroAtleta  - 1]  += 1          totalVotos  += 1     print 'Resultado da votacao:'     print 'Foram computados  %d  vo t os ' % t ot a lV ot os  print ' Jo g ador \ tVot o s\ t%%'  contador = 1  melhorJogador  = 0  for votosAtleta in  vot os Atl et as:        if  (v o to sA t le ta   > 0):          print '%d \t%d\ t% . 2f %%' %\                 (contador, votosAtleta, votosAtleta  / flo at (totalVotos) * 10 0 )          if ( vo tos At leta  > votosAtletas[melhorJogador]):              melhorJogador = co nt ad or  - 1      contador += 1     print 'O melhor jogador foi o numero  %d ,  c om   %d  votos, correspondendo a '\        '%. 2f  do total de votos' %\      (melhorJogador  + 1, votosAtletas[melhorJogador],          votosAtletas[melhorJogador] / float(totalVotos) * 100)