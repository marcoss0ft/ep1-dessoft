
def afundados(frota, tabuleiro):
    afundados = 0 
    for i in range(len(tabuleiro)):
        for k in range(len(tabuleiro[0])):
            if tabuleiro[i][k] == "X":
                for navio in frota:
                    for posicoes in frota[navio]:
                        if[i, k] in posicoes:
                            posicoes.remove([i, j])
                            if len(posicoes) == 0:
                                afundados += 1
                                del frota[navio]
                                break
                    if navio not in frota:
                        break
    return afundados