class Estado():
    def __init__(self, canibaisEsquerda, missionariosEsquerda, barco, canibaisDireita, missionariosDireita):
        self.canibaisEsquerda = canibaisEsquerda
        self.missionariosEsquerda = missionariosEsquerda
        self.barco = barco
        self.canibaisDireita = canibaisDireita
        self.missionariosDireita = missionariosDireita
        self.parent = None


def main():
    estadoInicial = Estado(3, 3, 1, 0, 0)

    percorrerMC(estadoInicial)


def percorrerMC(estado):
    print("Entrando metodo percorrerMC")
    print("(canibaisEsquerda,missionariosEsquerda,barco,canibaisDireita,missionariosDireita)")
    ce = estado.canibaisEsquerda
    me = estado.missionariosEsquerda
    cd = estado.canibaisDireita
    md = estado.missionariosDireita
    b = estado.barco

    print(f"{ce}, {me}, {b}, {cd}, {md}")


if __name__ == "__main__":
    main()
# Codigo china https://github.com/KevinNum1/IntelligentSearch
# Links Uteis
# http://www.inf.ufsc.br/grafos/temas/travessia/canibais.htm
# https://www.redblobgames.com/pathfinding/a-star/implementation.html
# https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2
# https://towardsdatascience.com/a-star-a-search-algorithm-eb495fb156bb
# https://gist.github.com/nenodias/d92b4cdbfb92ace257ff535856ba0a46