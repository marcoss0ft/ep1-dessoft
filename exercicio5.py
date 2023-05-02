def afundados(frota,tabuleiro):
    afundados = 0
    for embarcacoes in frota:
        for embarcacao in frota[embarcacoes]:
            i = 0
            for posicao in embarcacao:
                if not tabuleiro[posicao[0]][posicao[1]] == 'X':
                    break
                i += 1
            if i == len(embarcacao):
                afundados += 1
    return afundados