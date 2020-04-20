def son2str(posicao):
	return ' '.join([str(v) for v in posicao])

def estadoFinal(posicao):
	goal = False
	if posicao[0] == 0 and posicao[1] == 0 and posicao[3] == 0:
		goal = True
	return goal

def geraEstados(posicao):
    
    listaDeEstados = []
    
    #casos de ida
    #ir um missionario e um canibal
    estado = [posicao[0] -1, posicao[1] -1 , 0]
    listaDeEstados.append(estado)

    #ir dois missionarios
    estado = [posicao[0] -2, posicao[1], 0]
    listaDeEstados.append(estado)

    #ir dois canibais
    estado = [posicao[0], posicao[1] -2, 0]
    listaDeEstados.append(estado)

    #ir um missionario
    estado = [posicao[0] -1, posicao[1], 0]
    listaDeEstados.append(estado)

    #ir um canibal
    estado = [posicao[0], posicao[1] -1, 0]
    listaDeEstados.append(estado)

    #casos de volta
    #voltar um missionario e um canibal
    estado = [posicao[0] +1, posicao[1] +1 , 1]
    listaDeEstados.append(estado)

    #voltar dois missionarios
    estado = [posicao[0] +2, posicao[1], 1]
    listaDeEstados.append(estado)

    #voltar dois canibais
    estado = [posicao[0], posicao[1]+2, 1]
    listaDeEstados.append(estado)

    #voltar um missionário
    estado = [posicao[0] +1, posicao[1], 0]
    listaDeEstados.append(estado)

    #voltar um canibal
    estado = [posicao[0], posicao[1] +1, 0]
    listaDeEstados.append(estado)

    return listaDeEstados

def bfs(start):
	candidates = [start]
	fathers = dict()
	visited = [start]

	while len(candidates)>0:
		father = candidates[0]
		print("Lista de candidatos: ", candidates)
		del candidates[0]
		print("Visitado: ", father)
		if estadoFinal(father):
			res = []
			node = father
			while node != start:
				res.append(node)
				node = fathers[son2str(node)]
			res.append(start)
			res.reverse()
			print("Solucao encontrada: ", res)
		
		for son in geraEstados(father):
			if son not in visited:
				print("Enfileirado: ", son, father)
				visited.append(son)
				fathers[son2str(son)] = father
				candidates.append(son)

if __name__ == '__main__':
	bfs([3,3,1])