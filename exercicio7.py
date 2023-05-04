navios = {'porta-aviões': [1, 4], 'navio-tanque': [2, 3], 'contratorpedeiro': [3, 2], 'submarino': [4, 1]}
frota = {}

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

for navio, info in navios.items():
    quantidade = info[0]
    tamanho = info[1]
    print(f'Insira as informações referentes ao navio {navio} que possui tamanho {tamanho};')
    for n in range(quantidade):
        linha = int(input('Qual linha?\n'))
        coluna = int(input('Qual coluna?\n'))
        orientacao = 'vertical' if navio == 'submarino' else 'horizontal' if int(input('Qual orientação? (1 para vertical, 2 para horizontal)\n')) == 2 else 'vertical'
        while not posicao_valida(frota, linha, coluna, orientacao, tamanho):
            print('Esta posição não está válida!')
            linha = int(input('Qual linha?\n'))
            coluna = int(input('Qual coluna?\n'))
            orientacao = 'vertical' if navio == 'submarino' else 'horizontal' if int(input('Qual orientação? (1 para vertical, 2 para horizontal)\n')) == 2 else 'vertical'
        frota = preenche_frota(frota, navio, linha, coluna, orientacao, tamanho)

print(frota)
