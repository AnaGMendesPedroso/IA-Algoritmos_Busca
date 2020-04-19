# Acadêmicos:
# - Ana Gabrielly Mendes Pedroso
# - Davidson Denis Ferreira Guimaraes
# - Larissa Fraga Pinto
from src.depthfirst.No import No

class Grafo:

    def __init__(self, noInicial, movimentosPossiveis):
        self.noInicial = noInicial
        self.movimentosPossiveis = movimentosPossiveis
        self.LISTA_NOS = []
        self.LISTA_NOS.append(noInicial)


    def verificaSeNoJaFoiCriado(self, no):
        retorno = None

        for noAux in self.LISTA_NOS:
            if (no.getCanibais() == noAux.getCanibais() and no.getMissionarios() == noAux.getMissionarios() and no.getBote() == noAux.getBote()) :
                retorno = noAux
                break
        return retorno

    def gerarVizinhanca(self, noPai, movimentosPossiveis):
        for movimento in movimentosPossiveis:
            if (noPai.getMissionarios() - movimento[1]) > (noPai.getCanibais() - movimento[0]):
                noFilho = No(noPai.getCanibais() - movimento[0], noPai.getMissionarios() - movimento[1],
                             abs(noPai.getBote() - 1))
                resultado = self.verificaSeNoJaFoiCriado(noFilho)

                if resultado is None:
                    noFilho.setNoPai(noPai)
                    noPai.adicionaFilho(noFilho)
                    noFilho.adicionaPai(noPai)
                    self.LISTA_NOS.append(noFilho)
                else:
                    resultado.adicionaNoPai(noPai)