#Funções

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

def posiciona_frota(frota):
    grid = [[0 for _ in range(10)] for _ in range(10)] 
    for navio, posicoes in frota.items(): 
        for posicao in posicoes:
            for linha, coluna in posicao:
                grid[linha][coluna] = 1
    return grid

def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto

def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro

#Cria tabuleiros

frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

tabuleiro_oponente = posiciona_frota(frota_oponente)

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

tabuleiro_jogador = posiciona_frota(frota)

#jogo

jogando = True
while jogando:
    tabuleiros = monta_tabuleiros(tabuleiro_jogador,tabuleiro_oponente)
    print(tabuleiros)
    lista_posicoes_escolhidas = []
    verifica_posicao_inedita = True
    while verifica_posicao_inedita:
        valida_linha = True
        while valida_linha:
            linha_atacada  = int(input('Jogador, qual linha deseja atacar?'))
            if 0 <= linha_atacada:
                valida_linha = False
            else:
                print('Linha inválida!')
        valida_coluna = True
        while valida_coluna:
            coluna_atacada = int(input('Jogador, qual coluna deseja atacar?'))
            if 0 <= coluna_atacada <= 9:
                valida_coluna = False
            else:
                print('Coluna inválida!')
        posicao_escolhida = [linha_atacada,coluna_atacada]
        if posicao_escolhida not in lista_posicoes_escolhidas:
            lista_posicoes_escolhidas.append(posicao_escolhida)
            verifica_posicao_inedita = False
        else:
            print('A posição linha {0} e coluna {1} já foi informada anteriormente!'.format(linha_atacada,coluna_atacada))
        