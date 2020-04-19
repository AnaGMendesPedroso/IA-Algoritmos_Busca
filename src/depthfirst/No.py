# Acadêmicos:
# - Ana Gabrielly Mendes Pedroso
# - Davidson Denis Ferreira Guimaraes
# - Larissa Fraga Pinto
class No:

    def __init__(self, qtdCanibais, qtdMissionarios, qtdBoteMargemEsquerda):
        self.qtdCanibais = qtdCanibais
        self.qtdMissionarios = qtdMissionarios
        self.qtdBoteMargemEsquerda = qtdBoteMargemEsquerda
        self.foiVisitado = False
        self.listaNosPais = []
        self.listaNosFilhos = []

    def setNoPai(self, no):
        self.noPai = no

    def setFoiVisitado(self, check):
        self.foiVisitado = check

    def getCanibais(self):
        return self.qtdCanibais

    def getMissionarios(self):
        return self.qtdMissionarios

    def getBote(self):
        return self.qtdBoteMargemEsquerda

    def noValido(self):
        if (self.qtdCanibais > self.qtdMissionarios):
            return False
        else:
            return True

    def verificaSeEhUmNoObjetivo(self, estadoFinal):
        if (self.qtdCanibais == estadoFinal[0] and self.qtdMissionarios == estadoFinal[1] and self.qtdBoteMargemEsquerda == estadoFinal[2]):
            return True

    def adicionaPai(self, novoPai):
        self.listaNosPais.append(novoPai)

    def adicionaFilho(self, novoFilho):
        self.listaNosFilhos.append(novoFilho)