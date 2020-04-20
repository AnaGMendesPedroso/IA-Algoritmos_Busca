def son2str(pote):
	return ' '.join([str(v) for v in pote])

def estadoFinal(pote):
	goal = False
	if pote[0] == 4 or pote[1] == 4:
		goal = True
	return goal

def geraEstados(pote):

	listaDeEstados = []

	#esvaziar o pote 1
	estado = [0, pote[1]]
	listaDeEstados.append(estado)

	#esvaziar o pote 2
	estado = [pote[0], 0]
	listaDeEstados.append(estado)

	#encher o pote 1
	estado = [7, pote[1]]
	listaDeEstados.append(estado)

	#encher o pote 2
	estado = [pote[0], 5]
	listaDeEstados.append(estado)

	#verter pote 1 no pote 2
	if pote[0] >= 5-pote[1]:
		estado = [pote[0]-(5-pote[1]), 5]
	else:
		estado = [0, pote[1] + pote[0]]
	listaDeEstados.append(estado)

	#verter pote 2 no pote 1
	if pote[1] <= 7-pote[0]:
		estado = [pote[0]+pote[1],0]
	else:
		estado = [pote[0] + (7 - pote[0]), pote[1] - (7 - pote[0])]
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
	bfs([0,0])