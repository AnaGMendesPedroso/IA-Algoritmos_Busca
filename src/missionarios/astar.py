# Acadêmicos:
# - Ana Gabrielly Mendes Pedroso
# - Davidson Denis Ferreira Guimaraes
# - Larissa Fraga Pinto

import time

# Classe Estado que tem como objetivo mostrar o atual estado da transição
class Estado:
    def __init__(self, canibalEsquerda, missionarioEsquerda, barco, canibalDireita, missionarioDireita, action, h, g):
        self.canibalEsquerda = canibalEsquerda
        self.missionarioEsquerda = missionarioEsquerda
        self.barco = barco
        self.canibalDireita = canibalDireita
        self.missionarioDireita = missionarioDireita
        self.action = action
        self.h = h
        self.g = g
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


def successors(estado):
    children = list()
    if estado.barco == 'left':
        # send two missionaries from left to right
        novoEstado = Estado(estado.canibalEsquerda, estado.missionarioEsquerda - 2, 'right',
                          estado.canibalDireita, estado.missionarioDireita + 2,
                          "send two missionaries from left to right",
                          estado.canibalEsquerda + estado.missionarioEsquerda - 1, estado.g + 1)
        if novoEstado.is_valid():
            novoEstado.parent = estado
            children.append(novoEstado)

        # send two cannibals from left to right
        novoEstado = Estado(estado.canibalEsquerda - 2, estado.missionarioEsquerda, 'right',
                          estado.canibalDireita + 2, estado.missionarioDireita,
                          "send two cannibals from left to right",
                          estado.canibalEsquerda + estado.missionarioEsquerda - 1, estado.g + 1)
        if novoEstado.is_valid():
            novoEstado.parent = estado
            children.append(novoEstado)

        # send one missionary and one cannibal from left to right
        novoEstado = Estado(estado.canibalEsquerda - 1, estado.missionarioEsquerda - 1, 'right',
                          estado.canibalDireita + 1, estado.missionarioDireita + 1,
                          "send one missionary and one cannibal from left to right",
                          estado.canibalEsquerda + estado.missionarioEsquerda - 1, estado.g + 1)
        if novoEstado.is_valid():
            novoEstado.parent = estado
            children.append(novoEstado)

        # send one missionary from left to right
        novoEstado = Estado(estado.canibalEsquerda, estado.missionarioEsquerda - 1, 'right',
                          estado.canibalDireita, estado.missionarioDireita + 1,
                          "send one missionary from left to right",
                          estado.canibalEsquerda + estado.missionarioEsquerda - 1, estado.g + 1)
        if novoEstado.is_valid():
            novoEstado.parent = estado
            children.append(novoEstado)

        # send one cannibal from left to right
        novoEstado = Estado(estado.canibalEsquerda - 1, estado.missionarioEsquerda, 'right',
                          estado.canibalDireita + 1, estado.missionarioDireita,
                          "send one cannibal from left to right",
                          estado.canibalEsquerda + estado.missionarioEsquerda - 1, estado.g + 1)
        if novoEstado.is_valid():
            novoEstado.parent = estado
            children.append(novoEstado)
    else:
        # send two missionaries from right to left
        novoEstado = Estado(estado.canibalEsquerda, estado.missionarioEsquerda + 2, 'left',
                          estado.canibalDireita, estado.missionarioDireita - 2,
                          "send two missionaries from right to left",
                          estado.canibalEsquerda + estado.missionarioEsquerda - 1, estado.g + 1)
        if novoEstado.is_valid():
            novoEstado.parent = estado
            children.append(novoEstado)

        # send two cannibals from right to left
        novoEstado = Estado(estado.canibalEsquerda + 2, estado.missionarioEsquerda, 'left',
                          estado.canibalDireita - 2, estado.missionarioDireita,
                          "send two cannibals from right to left",
                          estado.canibalEsquerda + estado.missionarioEsquerda - 1, estado.g + 1)
        if novoEstado.is_valid():
            novoEstado.parent = estado
            children.append(novoEstado)

        # send one missionary and one cannibal from right to left
        novoEstado = Estado(estado.canibalEsquerda + 1, estado.missionarioEsquerda + 1, 'left',
                          estado.canibalDireita - 1, estado.missionarioDireita - 1,
                          "send one missionary and one cannibal from right to left",
                          estado.canibalEsquerda + estado.missionarioEsquerda - 1, estado.g + 1)
        if novoEstado.is_valid():
            novoEstado.parent = estado
            children.append(novoEstado)

        # send one missionary from right to left
        novoEstado = Estado(estado.canibalEsquerda, estado.missionarioEsquerda + 1, 'left',
                          estado.canibalDireita, estado.missionarioDireita - 1,
                          "send one missionary from right to left",
                          estado.canibalEsquerda + estado.missionarioEsquerda - 1, estado.g + 1)
        if novoEstado.is_valid():
            novoEstado.parent = estado
            children.append(novoEstado)

        # send one cannibal from right to left
        novoEstado = Estado(estado.canibalEsquerda + 1, estado.missionarioEsquerda, 'left',
                          estado.canibalDireita - 1, estado.missionarioDireita,
                          "send one cannibal from right to left",
                          estado.canibalEsquerda + estado.missionarioEsquerda - 1, estado.g + 1)
        if novoEstado.is_valid():
            novoEstado.parent = estado
            children.append(novoEstado)

    return children

# Heuristic: To come up with a heuristic we can try to solve a relaxed problem. If we do not take into
# account the possibility of cannibals eating missionaries, we can compute how many trips are
# needed to take everyone across. The boat takes two people, but after each trip across the
# boat has to come back to the starting side and so at least one person must paddle back. This
# will give us the following heuristic: number of people on initial side - 1


def a_star():
    initial_state = Estado(3, 3, 'left', 0, 0, "no action yet", 5, 0)

    if initial_state.is_goal():
        return initial_state

    frontier = list()
    visited = set()

    frontier.append(initial_state)

    while frontier:
        costs = list()
        for node in frontier:
            costs.append(node.h + node.g)
        index = costs.index(min(costs))
        state = frontier.pop(index)

        if state.is_goal():
            return state

        visited.add(state)

        children = successors(state)
        for child in children:
            if (child in visited) and (state.g < child.g):
                child.g = state.g
                child.parent = state
            elif (child in frontier) and (state.g < child.g):
                child.g = state.g
                child.parent = state
            else:
                frontier.append(child)
                child.g = state.g
    return None


def mostrarSolucao(solution):
    path = list()
    path.append(solution)
    parent = solution.parent

    while parent:
        path.append(parent)
        parent = parent.parent

    print("initial state: <3,3,left,0,0>")
    for i in range(1, len(path)):
        state = path[len(path) - i - 1]
        print ("action" + str(i) + ": " + state.action)
        if i == len(path)-1:
            print ("goal state" + str(i) + ": <" + str(state.canibalEsquerda) + "," + str(state.missionarioEsquerda) \
                  + "," + state.barco + "," + str(state.canibalDireita) + "," + \
                  str(state.missionarioDireita) + ">")
        else:
            print ("state" + str(i) + ": <" + str(state.canibalEsquerda) + "," + str(state.missionarioEsquerda) \
              + "," + state.barco + "," + str(state.canibalDireita) + "," + \
              str(state.missionarioDireita) + ">")


def main():

    solucao = a_star()
    print("( Canibais esquerda, Missionarios esquerda, posicao barco, Canibais Direita, Missionarios Direita )")
    mostrarSolucao(solucao)


# if called from the command line, call main()
if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s segundos ---" % (time.time() - start_time))
