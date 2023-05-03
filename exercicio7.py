navios = ['porta-aviões','navio-tanque','contratorpedeiro','submarino']
tamanhos = [4,3,2,1]
quantidades = [1,2,3,4]
i = 0
for navio in navios:
    print('\nInsira as informações referentes ao navio {0} que possui tamanho {1};\n'.format(navio,tamanhos[i]))
    for n in range (quantidades[i]):
        linha = int(input('\nQual linha?\n'))
        coluna = int(input('\nQual coluna?\n'))
        orientacao = int(input('\nQual orientacao?\n'))