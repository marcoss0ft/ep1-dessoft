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
frota = {}
dic_orientacoes = {1:'vertical',2:'horizontal'}

for navio in navios:
    quantidade = navios[navio][0]
    tamanho = navios[navio][1]
    for n in range (quantidade):
        verificando = True
        while verificando:
            print('Insira as informações referentes ao navio {0} que possui tamanho {1}'.format(navio,tamanho))
            linha = int(input('Linha:'))
            coluna = int(input('Coluna:'))
            if navio != 'submarino':
                vertical_horizontal = int(input('[1] Vertical [2] Horizontal:'))
                orientacao = dic_orientacoes[vertical_horizontal]
            validacao = posicao_valida(frota,linha,coluna,orientacao,tamanho)
            if validacao == True:
                frota = preenche_frota(frota,navio,linha,coluna,orientacao,tamanho)
                verificando = False
            else:
                print('Esta posição não está válida!')


print(frota)