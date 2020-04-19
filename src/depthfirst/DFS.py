# Acadêmicos:
# - Ana Gabrielly Mendes Pedroso
# - Davidson Denis Ferreira Guimaraes
# - Larissa Fraga Pinto
from src.depthfirst.Grafo import *
from src.depthfirst.No import *

class DFS:

    def __init__(self,estadoInicial, estadoFinal ,movimentosPossiveis):
        self.pilha = []
        self.pilha.append(estadoInicial)
        self.grafo = Grafo(estadoInicial, movimentosPossiveis)
        self.estadoFinal = estadoFinal


    def formataSaida(self, s):
        return ' '.join([str(v) for v in s])

    def buscaEmProfundidade(self,no, movimentosPossiveis):
        if no.verificaSeEhUmNoObjetivo(self.estadoFinal):
    #           printar caminho
            print("SEI LÁ..")
        else:
            self.grafo.gerarVizinhanca(no,movimentosPossiveis)
    #         iterar sobre os filhos do no (vizinhança) e empilhar cada nó
        self.buscaEmProfundidade(self.pilha.pop(), movimentosPossiveis)

    if __name__ == '__main__':
        movimentosPossiveis = [[0, 1], [1, 0], [0, 2], [2, 0], [1, 1]]
        noInicial = No(3, 3, 1)
        buscaEmProfundidade(noInicial, movimentosPossiveis)