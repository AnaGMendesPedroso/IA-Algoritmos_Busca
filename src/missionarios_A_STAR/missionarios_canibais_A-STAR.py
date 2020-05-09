class Estado():
    def __init__(self, canibaisEsquerda, missionariosEsquerda, canibaisDireita, missionariosDireita):
        self.canibaisEsquerda = canibaisEsquerda
        self.missionariosEsquerda = missionariosEsquerda
        self.barcoEsquerda = 1
        self.barcoDireita = 0
        self.canibaisDireita = canibaisDireita
        self.missionariosDireita = missionariosDireita
        self.parent = None


def main():
    estadoInicial = Estado(3, 3, 0, 0)

    percorrerMC(estadoInicial)


def percorrerMC(estado):
    print("Entrando metodo percorrerMC")
    printEstado(estado)
    # print("(canibaisEsquerda,missionariosEsquerda,barcoEsquerda  || barcoDireita ,canibaisDireita,missionariosDireita)")
    # ce = estado.canibaisEsquerda
    # me = estado.missionariosEsquerda
    # cd = estado.canibaisDireita
    # md = estado.missionariosDireita
    # bd = estado.barcoDireita
    # be = estado.barcoEsquerda

    # print(f"{ce}, {me}, {be} || {bd}, {cd}, {md}")
    #enviar todos os missionarios e canibais para a esquerda
    auxCanibaisEsquerda = estado.canibaisEsquerda
    auxMissionariosEsquerda = estado.missionariosEsquerda

    while (verificarCondicaoDeParada(estado)):


def verificarMovimentosPossiveis(estado):
    if(estado.missionariosEsquerda > estado.missionariosDireita):
        


def printEstado(estado):
    print("(canibaisEsquerda,missionariosEsquerda,barcoEsquerda  || barcoDireita ,canibaisDireita,missionariosDireita)")
    ce = estado.canibaisEsquerda
    me = estado.missionariosEsquerda
    cd = estado.canibaisDireita
    md = estado.missionariosDireita
    bd = estado.barcoDireita
    be = estado.barcoEsquerda
    
    print(f"{ce}, {me}, {be} || {bd}, {cd}, {md}")


def verificarCondicaoDeParada(estado):
    if(estado.canibaisEsquerda != 0 & estado.missionariosEsquerda != 0):
        return False
    return True


if __name__ == "__main__":
    main()
# Codigo china https://github.com/KevinNum1/IntelligentSearch
# Links Uteis
# http://www.inf.ufsc.br/grafos/temas/travessia/canibais.htm
# https://www.redblobgames.com/pathfinding/a-star/implementation.html
# https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2
# https://towardsdatascience.com/a-star-a-search-algorithm-eb495fb156bb
# https://gist.github.com/nenodias/d92b4cdbfb92ace257ff535856ba0a46