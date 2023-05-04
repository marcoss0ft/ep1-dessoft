def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    if orientacao == "vertical":
        for i in range(tamanho):
            posicoes.append([linha+i, coluna])
    elif orientacao == "horizontal":
        for i in range(tamanho):
            posicoes.append([linha, coluna+i])
    return posicoes

def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):

    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    

    if nome_navio in frota:
        frota[nome_navio].append(posicoes)
    else:
        frota[nome_navio] = [posicoes]
    
    return frota

def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    posicoes_navio = define_posicoes(linha, coluna, orientacao, tamanho)

 
    for navio in frota.values():
        for posicoes_ocupadas in navio:
            for posicao in posicoes_navio:
                if posicao in posicoes_ocupadas:
                    return False

    for posicao in posicoes_navio:
        if posicao[0] < 0 or posicao[0] > 9 or posicao[1] < 0 or posicao[1] > 9:
            return False
    
    return True

navios = {'porta-aviões':[1,4],'navio-tanque':[2,3],'contratorpedeiro':[3,2],'submarino':[4,1]}
i = 0
frota = {}
orientacoes = ['vertical','horizontal']


for navio in navios:
    quantidade = navios[navio][0]
    tamanho = navios[navio][1]
    for n in range (quantidade):
        verificando = True
        while verificando:
            print('\nInsira as informações referentes ao navio {0} que possui tamanho {1}\n'.format(navio,tamanho))
            linha = int(input('\nQual linha?\n'))
            coluna = int(input('\nQual coluna?\n'))
            if navio != 'submarino':
                orientacao = int(input('\n[1] Vertical [2] Horizontal >'))
                if orientacao == 1:
                    orientacao = 'vertical'
                elif orientacao == 2:
                    orientacao = 'horizontal'
            else:
                orientacao = 'vertical'
            validacao = posicao_valida(frota,linha,coluna,orientacao,tamanho)
            if validacao == True and orientacao in orientacoes:
                frota = preenche_frota(frota,navio,linha,coluna,orientacao,tamanho)
                verificando = False
            else:
                print('\nEsta posição não está válida!\n')


print(frota)