import src.depthfirst.dfs

movimentos_validos = []
mov1 = src.depthfirst.dfs.Movimento(1,0)
mov2 = src.depthfirst.dfs.Movimento(2,0)
mov3 = src.depthfirst.dfs.Movimento(0,1)
mov4 = src.depthfirst.dfs.Movimento(0,2)
mov5 = src.depthfirst.dfs.Movimento(1,1)

movimentos_validos.append(mov1)
movimentos_validos.append(mov2)
movimentos_validos.append(mov3)
movimentos_validos.append(mov4)
movimentos_validos.append(mov5)

no_inicial = src.depthfirst.dfs.No(3, 3, 1)
no_final = src.depthfirst.dfs.No(0, 0, 0)
grafo = src.depthfirst.dfs.Grafo(no_inicial, no_final, movimentos_validos)
grafo.gerar_grafo()
dfs = src.depthfirst.dfs.DFS(no_inicial, no_final, movimentos_validos)
dfs.busca_em_profundidade()
