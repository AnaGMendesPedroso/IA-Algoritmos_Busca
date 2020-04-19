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

    def set_foi_visitado(self):
        self.foiVisitado = True

    def get_foi_visitado(self):
        return self.foiVisitado

    def get_canibais(self):
        return self.qtdCanibais

    def get_missionarios(self):
        return self.qtdMissionarios

    def get_bote(self):
        return self.qtdBoteMargemEsquerda

    def get_lista_pais(self):
        return self.listaNosPais

    def get_lista_filhos(self):
        return self.listaNosFilhos

    def verifica_se_eh_no_objetivo(self, estadoFinal):
        if self.qtdCanibais == estadoFinal[0] \
                and self.qtdMissionarios == estadoFinal[1] \
                and self.qtdBoteMargemEsquerda == estadoFinal[2]:
            return True

    def verifica_validade(self, no_pai):
        if no_pai.get_bote() == 0 and self.get_canibais() + no_pai.get_canibais() > self.get_missionarios():
            return False
        elif no_pai.get_bote() == 1 and (self.get_canibais() > self.get_missionarios()):
            return False
        else:
            return True

    def adiciona_pai(self, novopai):
        self.listaNosPais.append(novopai)

    def adiciona_filho(self, novofilho):
        self.listaNosFilhos.append(novofilho)


class Grafo:

    def __init__(self, noInicial, movimentosPossiveis):
        self.noInicial = noInicial
        self.movimentosPossiveis = movimentosPossiveis
        self.LISTA_NOS = []
        self.LISTA_NOS.append(noInicial)

    def verifica_se_no_ja_foi_criado(self, no):
        verificacao = None

        for noAux in self.LISTA_NOS:
            if no.get_canibais() == noAux.get_canibais() and no.get_missionarios() == noAux.get_missionarios() and no.get_bote() == noAux.get_bote():
                verificacao = noAux
                break
        return verificacao

    def gerar_nos_filhos(self, no_pai, movimentos_possiveis):
        for movimento in movimentos_possiveis:
            if no_pai.get_bote() == 1:
                subtrai_canibais = no_pai.get_canibais() - movimento.get_canibais_no_barco()
                subtrai_missionarios = no_pai.get_missionarios() - movimento.get_missionarios_no_barco()
                if subtrai_canibais >= 0 and subtrai_missionarios >= 0:
                    self.cria_no(subtrai_canibais, subtrai_missionarios, 0, no_pai)
            else:
                soma_canibais = no_pai.get_canibais() + movimento.get_canibais_no_barco()
                soma_missionarios = no_pai.get_missionarios() + movimento.get_missionarios_no_barco()
                if soma_canibais <= self.noInicial.get_canibais() \
                        and soma_missionarios <= self.noInicial.get_missionarios():
                    self.cria_no(soma_canibais, soma_missionarios, 1, no_pai)

    def cria_no(self, qtdCanib ,qtdMissio, posicaoBote, no_pai):
        no_filho = No(qtdCanib, qtdMissio, posicaoBote)

        validade = no_filho.verifica_validade(no_pai)
        if validade:
            resultado = self.verifica_se_no_ja_foi_criado(no_filho)
            if resultado is None:
                no_filho.adiciona_pai(no_pai)
                no_pai.adiciona_filho(no_filho)
                self.LISTA_NOS.append(no_filho)
            else:
                resultado.adiciona_pai(no_pai)

class DFS:

    def __init__(self, estadoInicial, estadoFinal, movimentosPossiveis):
        self.candidatos = []
        self.fronteira = []
        self.grafo = Grafo(estadoInicial, movimentosPossiveis)
        self.estadoFinal = estadoFinal
        self.estadoInicial = estadoInicial
        self.candidatos.append(estadoInicial)

    def printa_fronteira(self):
        for no in self.fronteira:
            print(self.formata_saida(no))
        print('-'*30)

    def printa_candidatos(self):
        for no in self.candidatos:
            print(self.formata_saida(no))
        print('-'*30)

    def formata_saida(self, no):
        return '[' + str(no.get_canibais()) + ',' + str(no.get_missionarios()) + ',' + str(no.get_bote()) + ']'

    def busca_em_profundidade(self, no, movimentosPossiveis):
        if len(self.candidatos) == 0:
            print("\nNós percorridos:")
            self.printa_fronteira()

        elif no.get_canibais() == self.estadoFinal.get_canibais() \
                and no.get_missionarios() == self.estadoFinal.get_missionarios() \
                and no.get_bote() == self.estadoFinal.get_bote():
            print('#' * 30)
            print("SOLUÇÃO ENCONTRADA: ")
            self.printa_fronteira()
            print('#' * 30)

        else:
            if not no.get_foi_visitado():
                print("\nNó desempilhado:")
                print(self.formata_saida(no))
                self.fronteira.append(no)
                no.set_foi_visitado()

            self.grafo.gerar_nos_filhos(no, movimentosPossiveis)
            for noFilho in no.get_lista_filhos():
                if not self.candidatos.__contains__(noFilho):
                    self.candidatos.append(noFilho)

            print("\nNós candidatos empilhados:")
            self.printa_candidatos()
            self.busca_em_profundidade(self.candidatos.pop(), movimentosPossiveis)


class Movimento:

    def __init__(self, qtd_canibais_no_barco, qtd_missionarios_no_barco):
        self.qtd_canibais_no_barco = qtd_canibais_no_barco
        self.qtd_missionarios_no_barco = qtd_missionarios_no_barco

    def get_canibais_no_barco(self):
        return self.qtd_canibais_no_barco

    def get_missionarios_no_barco(self):
        return self.qtd_missionarios_no_barco
