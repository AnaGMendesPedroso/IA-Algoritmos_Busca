import src.missionarios_dfs.dfs

movimentos_validos = []
mov1 = src.missionarios_dfs.dfs.Movimento(1, 0)
mov2 = src.missionarios_dfs.dfs.Movimento(2, 0)
mov3 = src.missionarios_dfs.dfs.Movimento(0, 1)
mov4 = src.missionarios_dfs.dfs.Movimento(0, 2)
mov5 = src.missionarios_dfs.dfs.Movimento(1, 1)

movimentos_validos.append(mov1)
movimentos_validos.append(mov2)
movimentos_validos.append(mov3)
movimentos_validos.append(mov4)
movimentos_validos.append(mov5)

no_inicial = src.missionarios_dfs.dfs.No(3, 3, 1)
no_final = src.missionarios_dfs.dfs.No(0, 0, 0)
grafo = src.missionarios_dfs.dfs.Grafo(no_inicial, no_final, movimentos_validos)
grafo.gerar_grafo()
dfs = src.missionarios_dfs.dfs.DFS(grafo.get_lista_nos_grafo(), no_inicial, no_final)
dfs.busca_em_profundidade()
