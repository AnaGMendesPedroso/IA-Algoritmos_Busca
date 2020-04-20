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

    def verifica_validade(self, movimento):
        verificacao = False
        canibais_oposto = 3 - self.get_canibais()
        missionarios_oposto = 3 - self.get_missionarios()

        if 0 <= self.get_canibais() <= 3 and 0 <= self.get_missionarios() <= 3 \
                and (self.get_missionarios() == 0
                     or self.get_missionarios() == 3
                     or self.get_missionarios() == self.get_canibais()):

            verificacao = True

        return verificacao

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

    def gerar_nos_filhos(self, no_pai):
        for movimento in self.movimentosPossiveis:
            canibais = 0
            missionarios = 0
            no_filho = None

            if no_pai.get_bote() == 1:
                canibais = no_pai.get_canibais() - movimento.get_canibais_no_barco()
                missionarios = no_pai.get_missionarios() - movimento.get_missionarios_no_barco()
                if 0 <= canibais <= 3 and 0 <= missionarios <= 3:
                    no_filho = No(canibais, missionarios, 0)
                    self.geracao_final(movimento, no_filho, no_pai)

            else:
                canibais = no_pai.get_canibais() + movimento.get_canibais_no_barco()
                missionarios = no_pai.get_missionarios() + movimento.get_missionarios_no_barco()
                if 0 <= canibais <= 3 and 0 <= missionarios <= 3:
                    no_filho = No(canibais, missionarios, 1)
                    self.geracao_final(movimento, no_filho, no_pai)

    def geracao_final(self, movimento, no_filho, no_pai):
        validade = no_filho.verifica_validade(movimento)
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
        self.contador_solucao_encontrada = 0
        self.grafo = Grafo(estadoInicial, movimentosPossiveis)
        self.estadoFinal = estadoFinal
        self.estadoInicial = estadoInicial
        self.candidatos.append(estadoInicial)

    def printa_fronteira(self):
        for no in self.fronteira:
            print(self.formata_saida(no))
        print('-' * 30)

    def printa_candidatos(self):
        for no in self.candidatos:
            print(self.formata_saida(no))
        print('-' * 30)

    def formata_saida(self, no):
        return '[' + str(no.get_canibais()) + ',' + str(no.get_missionarios()) + ',' + str(no.get_bote()) + ']'

    def busca_em_profundidade(self):
        if len(self.candidatos) > 0:
            no = self.candidatos.pop()
            if no.get_canibais() == self.estadoFinal.get_canibais() and no.get_missionarios() == self.estadoFinal.get_missionarios() and no.get_bote() == self.estadoFinal.get_bote():
                self.contador_solucao_encontrada += 1
                print('#' * 30)
                print('SOLUÇÃO ENCONTRADA: ')
                self.printa_fronteira()
                print(self.formata_saida(self.estadoFinal))
                print('#' * 30)

            if not no.get_foi_visitado():
                print("\nNó desempilhado e adicionado a fronteira:")
                print(self.formata_saida(no))
                self.fronteira.append(no)
                no.set_foi_visitado()

            self.grafo.gerar_nos_filhos(no)
            for noFilho in no.get_lista_filhos():
                if not self.candidatos.__contains__(noFilho):
                    self.candidatos.append(noFilho)

            print("\nNós candidatos empilhados:")
            self.printa_candidatos()
            self.busca_em_profundidade()
        else:
            print("Não foi possível atingir o estado final desejado\n Estado final: " + self.formata_saida(
                self.estadoFinal))


class Movimento:

    def __init__(self, qtd_canibais_no_barco, qtd_missionarios_no_barco):
        self.qtd_canibais_no_barco = qtd_canibais_no_barco
        self.qtd_missionarios_no_barco = qtd_missionarios_no_barco

    def get_canibais_no_barco(self):
        return self.qtd_canibais_no_barco

    def get_missionarios_no_barco(self):
        return self.qtd_missionarios_no_barco
