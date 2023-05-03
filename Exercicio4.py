def posiciona_frota(frota):
    grid = [[0 for _ in range(10)] for _ in range(10)] 
    for navio, posicoes in frota.items(): 
        for posicao in posicoes:
            for linha, coluna in posicao:
                grid[linha][coluna] = 1
    return grid

