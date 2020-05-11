# Acadêmicos:
# - Ana Gabrielly Mendes Pedroso
# - Davidson Denis Ferreira Guimaraes
# - Larissa Fraga Pinto

import time

# Classe Estado que tem como objetivo mostrar o atual estado da transição
class Estado:
    def __init__(self, canibalEsquerda, missionarioEsquerda, barco, canibalDireita, missionarioDireita, action, movimentosPossiveis, custoPorMovimento):
        self.canibalEsquerda = canibalEsquerda
        self.missionarioEsquerda = missionarioEsquerda
        self.barco = barco
        self.canibalDireita = canibalDireita
        self.missionarioDireita = missionarioDireita
        self.action = action
        self.movimentosPossiveis = movimentosPossiveis
        self.custoPorMovimento = custoPorMovimento
        self.parent = None

    def is_goal(self):
        if self.canibalEsquerda == 0 and self.missionarioEsquerda == 0:
            return True
        else:
            return False

    def is_valid(self):
        if self.missionarioEsquerda >= 0 and self.missionarioDireita >= 0 \
                and self.canibalEsquerda >= 0 and self.canibalDireita >= 0 \
                and (self.missionarioEsquerda == 0 or self.missionarioEsquerda >= self.canibalEsquerda) \
                and (self.missionarioDireita == 0 or self.missionarioDireita >= self.canibalDireita):
            return True
        else:
            return False

    def __eq__(self, other):
        return self.canibalEsquerda == other.canibalEsquerda and self.missionarioEsquerda == other.missionarioEsquerda \
               and self.barco == other.barco and self.canibalDireita == other.canibalDireita \
               and self.missionarioDireita == other.missionarioDireita

    def __hash__(self):
        return hash((self.canibalEsquerda, self.missionarioEsquerda, self.barco, self.canibalDireita, self.missionarioDireita))


def sucessores(estado):
    children = list()
    if estado.barco == 'left':

        # envia dois missionarios da esquerda para direita
        novoEstado = Estado(estado.canibalEsquerda, estado.missionarioEsquerda - 2, 'right',
                          estado.canibalDireita, estado.missionarioDireita + 2,
                          "envia dois missionarios da esquerda para direita",
                          estado.canibalEsquerda + estado.missionarioEsquerda - 1, estado.custoPorMovimento + 1)
        if novoEstado.is_valid():
            novoEstado.parent = estado
            children.append(novoEstado)

        # envia dois canibais da esquerda para direita
        novoEstado = Estado(estado.canibalEsquerda - 2, estado.missionarioEsquerda, 'right',
                          estado.canibalDireita + 2, estado.missionarioDireita,
                          "envia dois canibais da esquerda para direita",
                          estado.canibalEsquerda + estado.missionarioEsquerda - 1, estado.custoPorMovimento + 1)
        if novoEstado.is_valid():
            novoEstado.parent = estado
            children.append(novoEstado)

        # envia um missionario e um canibal da esquerda para direita
        novoEstado = Estado(estado.canibalEsquerda - 1, estado.missionarioEsquerda - 1, 'right',
                          estado.canibalDireita + 1, estado.missionarioDireita + 1,
                          "envia um missionario e um canibal da esquerda para direita",
                          estado.canibalEsquerda + estado.missionarioEsquerda - 1, estado.custoPorMovimento + 1)
        if novoEstado.is_valid():
            novoEstado.parent = estado
            children.append(novoEstado)

        # envia um missionario da esquerda para a direita
        novoEstado = Estado(estado.canibalEsquerda, estado.missionarioEsquerda - 1, 'right',
                          estado.canibalDireita, estado.missionarioDireita + 1,
                          "envia um missionario da esquerda para a direita",
                          estado.canibalEsquerda + estado.missionarioEsquerda - 1, estado.custoPorMovimento + 1)
        if novoEstado.is_valid():
            novoEstado.parent = estado
            children.append(novoEstado)

        # envia um canibal da esquerda para a direita
        novoEstado = Estado(estado.canibalEsquerda - 1, estado.missionarioEsquerda, 'right',
                          estado.canibalDireita + 1, estado.missionarioDireita,
                          "envia um canibal da esquerda para a direita",
                          estado.canibalEsquerda + estado.missionarioEsquerda - 1, estado.custoPorMovimento + 1)
        if novoEstado.is_valid():
            novoEstado.parent = estado
            children.append(novoEstado)
    else:
        # envia dois missionarios da direita para esquerda
        novoEstado = Estado(estado.canibalEsquerda, estado.missionarioEsquerda + 2, 'left',
                          estado.canibalDireita, estado.missionarioDireita - 2,
                          "envia dois missionarios da direita para esquerda",
                          estado.canibalEsquerda + estado.missionarioEsquerda - 1, estado.custoPorMovimento + 1)
        if novoEstado.is_valid():
            novoEstado.parent = estado
            children.append(novoEstado)

        # envia dois canibais da direita para a esquerda
        novoEstado = Estado(estado.canibalEsquerda + 2, estado.missionarioEsquerda, 'left',
                          estado.canibalDireita - 2, estado.missionarioDireita,
                          "envia dois canibais da direita para a esquerda",
                          estado.canibalEsquerda + estado.missionarioEsquerda - 1, estado.custoPorMovimento + 1)
        if novoEstado.is_valid():
            novoEstado.parent = estado
            children.append(novoEstado)

        # envia um missionario e um canibal da direita para esquerda
        novoEstado = Estado(estado.canibalEsquerda + 1, estado.missionarioEsquerda + 1, 'left',
                          estado.canibalDireita - 1, estado.missionarioDireita - 1,
                          "envia um missionario e um canibal da direita para esquerda",
                          estado.canibalEsquerda + estado.missionarioEsquerda - 1, estado.custoPorMovimento + 1)
        if novoEstado.is_valid():
            novoEstado.parent = estado
            children.append(novoEstado)

        # envia uma missionario da direita para a esquerda
        novoEstado = Estado(estado.canibalEsquerda, estado.missionarioEsquerda + 1, 'left',
                          estado.canibalDireita, estado.missionarioDireita - 1,
                          "envia uma missionario da direita para a esquerda",
                          estado.canibalEsquerda + estado.missionarioEsquerda - 1, estado.custoPorMovimento + 1)
        if novoEstado.is_valid():
            novoEstado.parent = estado
            children.append(novoEstado)

        # envia um canibal da direita para a esquerda
        novoEstado = Estado(estado.canibalEsquerda + 1, estado.missionarioEsquerda, 'left',
                          estado.canibalDireita - 1, estado.missionarioDireita,
                          "envia um canibal da direita para a esquerda",
                          estado.canibalEsquerda + estado.missionarioEsquerda - 1, estado.custoPorMovimento + 1)
        if novoEstado.is_valid():
            novoEstado.parent = estado
            children.append(novoEstado)

    return children


def algoritmoASTAR():
    estadoInicial = Estado(3, 3, 'left', 0, 0, "Sem movimentos", 5, 0)

    if estadoInicial.is_goal():
        return estadoInicial

    fronteira = list()
    visitado = set()

    fronteira.append(estadoInicial)

    while fronteira:
        custo = list()
        for node in fronteira:
            custo.append(node.movimentosPossiveis + node.custoPorMovimento)
        index = custo.index(min(custo))
        estado = fronteira.pop(index)

        if estado.is_goal():
            return estado

        visitado.add(estado)

        filhos = sucessores(estado)
        for filho in filhos:
            if (filho in visitado) and (estado.custoPorMovimento < filho.custoPorMovimento):
                filho.custoPorMovimento = estado.custoPorMovimento
                filho.parent = estado
            elif (filho in fronteira) and (estado.custoPorMovimento < filho.custoPorMovimento):
                filho.custoPorMovimento = estado.custoPorMovimento
                filho.parent = estado
            else:
                fronteira.append(filho)
                filho.custoPorMovimento = estado.custoPorMovimento
    return None


def mostrarSolucao(solucao):
    path = list()
    path.append(solucao)
    parent = solucao.parent

    while parent:
        path.append(parent)
        parent = parent.parent

    print("Estado inicial: <3,3,1,0,0>")
    print (34 * "-")

    for i in range(1, len(path)):
        estado = path[len(path) - i - 1]

        if(estado.barco == 'left'):
            if i == len(path)-1:
                print ("Estado Final " + str(i) + ": <" + str(estado.canibalEsquerda) + "," + str(estado.missionarioEsquerda) \
                    + ",1," + str(estado.canibalDireita) + "," + \
                    str(estado.missionarioDireita) + ">")
            else:
                print ("Estado " + str(i) + ": <" + str(estado.canibalEsquerda) + "," + str(estado.missionarioEsquerda) \
                + ",1," + str(estado.canibalDireita) + "," + \
                str(estado.missionarioDireita) + ">")
        else:
            if i == len(path)-1:
                print ("Estado Final " + str(i) + ": <" + str(estado.canibalEsquerda) + "," + str(estado.missionarioEsquerda) \
                    + ",0," + str(estado.canibalDireita) + "," + \
                    str(estado.missionarioDireita) + ">")
            else:
                print ("Estado " + str(i) + ": <" + str(estado.canibalEsquerda) + "," + str(estado.missionarioEsquerda) \
                + ",0," + str(estado.canibalDireita) + "," + \
                str(estado.missionarioDireita) + ">")
        print (34 * "-")


def main():

    solucao = algoritmoASTAR()
    print("( Canibais esquerda, Missionarios esquerda, posicao barco, Canibais Direita, Missionarios Direita )")
    mostrarSolucao(solucao)


# MAIN 
if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s segundos ---" % (time.time() - start_time))
