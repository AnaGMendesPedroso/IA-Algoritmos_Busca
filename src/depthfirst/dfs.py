# Acadêmicos:
# - Ana Gabrielly Mendes Pedroso
# - Davidson Denis Ferreira Guimaraes
# - Larissa Fraga Pinto

def formata_saida(no):
    return '[' + str(no.get_canibais()) + ',' + str(no.get_missionarios()) + ',' + str(no.get_bote()) + ']'


def compara_nos(no1, no2):
    comparacao = False
    if no1.get_canibais() == no2.get_canibais() \
            and no1.get_missionarios() == no2.get_missionarios() \
            and no1.get_bote() == no2.get_bote():
        comparacao = True

    return comparacao


class No:

    def __init__(self, qtdCanibais, qtdMissionarios, qtdBoteMargemEsquerda):
        self.qtdCanibais = qtdCanibais
        self.qtdMissionarios = qtdMissionarios
        self.qtdBoteMargemEsquerda = qtdBoteMargemEsquerda
        self.solucao_que_foi_visitado = []
        self.listaNosPais = []
        self.listaNosFilhos = []

    def adiciona_solucao_que_foi_visitado(self, id_solucao, ordem):
        sol = [id_solucao, ordem]
        self.solucao_que_foi_visitado.append(sol)

    def get_solucao_que_foi_visitado(self):
        return self.solucao_que_foi_visitado

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

    def verifica_validade(self):
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
        if self.pai_nao_eh_filho(novopai):
            self.listaNosPais.append(novopai)

    def adiciona_filho(self, novofilho):
        if self.filho_nao_eh_pai(novofilho):
            self.listaNosFilhos.append(novofilho)

    def pai_nao_eh_filho(self, pai):
        verificacao = True
        for no in self.get_lista_filhos():
            if compara_nos(no, pai):
                verificacao = False
        return verificacao

    def filho_nao_eh_pai(self, novofilho):
        verificacao = True
        for no in self.get_lista_pais():
            if compara_nos(no, novofilho):
                verificacao = False
        return verificacao


class Grafo:

    def __init__(self, noInicial,noFinal, movimentosPossiveis):
        self.noInicial = noInicial
        self.noFinal = noFinal
        self.movimentosPossiveis = movimentosPossiveis
        self.LISTA_NOS = []
        self.LISTA_NOS.append(noInicial)

    def get_lista_nos_grafo(self):
        return self.LISTA_NOS

    def gerar_grafo(self):
        for no in self.LISTA_NOS:
            self.gerar_nos_filhos(no)

        print('Estados do grafo gerado')
        for no in self.LISTA_NOS:
            print(formata_saida(no) + ' Filhos: '+' '.join([str(formata_saida(v)) for v in no.get_lista_filhos()]) + '\n\t\tPais: '+' '.join([str(formata_saida(v)) for v in no.get_lista_pais()]))
        print('='*30)

    def gerar_nos_filhos(self, no_pai):
        if not compara_nos(no_pai, self.noFinal):
            for movimento in self.movimentosPossiveis:
                canibais = 0
                missionarios = 0
                bote = -1
                no_filho = None

                if no_pai.get_bote() == 1:
                    canibais = no_pai.get_canibais() - movimento.get_canibais_no_barco()
                    missionarios = no_pai.get_missionarios() - movimento.get_missionarios_no_barco()
                    bote = 0

                else:
                    canibais = no_pai.get_canibais() + movimento.get_canibais_no_barco()
                    missionarios = no_pai.get_missionarios() + movimento.get_missionarios_no_barco()
                    bote = 1

                if 0 <= canibais <= 3 and 0 <= missionarios <= 3:
                    no_filho = No(canibais, missionarios, bote)
                    if not compara_nos(no_filho, self.noInicial):
                        if no_filho.verifica_validade():
                            self.geracao_final(no_filho, no_pai)

    def geracao_final(self, no_recem_criado, novo_pai):
        no_ja_foi_criado = False
        for no_grafo in self.LISTA_NOS:
            for no_filho_grafo in no_grafo.get_lista_filhos():
                if compara_nos(no_recem_criado, no_filho_grafo):
                    no_ja_foi_criado = True
                    no_filho_grafo.adiciona_pai(novo_pai)
                    novo_pai.adiciona_filho(no_filho_grafo)
                    break
            if no_ja_foi_criado:
                break

        if not no_ja_foi_criado:
            no_recem_criado.adiciona_pai(novo_pai)
            novo_pai.adiciona_filho(no_recem_criado)
            self.LISTA_NOS.append(no_recem_criado)


class DFS:

    def __init__(self, grafo, estadoInicial, estadoFinal):
        self.fronteira = []
        self.nos_visitados = []
        self.contador_solucao_encontrada = 1
        self.ordem_de_visita = 1
        self.estadoInicial = estadoInicial
        self.estadoFinal = estadoFinal
        self.grafo = grafo
        self.fronteira.append(estadoInicial)

    def printa_nos_visitados(self, solucao, ordem):
        aux = 1
        for no in self.grafo:
            momentos = no.get_solucao_que_foi_visitado()
            for sol in momentos:
                if aux <= ordem and sol[0] <= solucao and sol[1] == aux:
                    print(formata_saida(no))
                    aux = aux + 1
                    break

    def printa_fronteira(self):
        for no in self.fronteira:
            print(formata_saida(no))

    def busca_em_profundidade(self):
        if len(self.fronteira) > 0:
            no = self.fronteira.pop()

            print("\nNó que será visitado:")
            print(formata_saida(no))
            print("\nFronteira antes da visita:")
            self.printa_fronteira()
            self.nos_visitados.append(no)
            no.adiciona_solucao_que_foi_visitado(self.contador_solucao_encontrada, self.ordem_de_visita)
            self.ordem_de_visita += 1
            self.coloca_filhos_na_fronteira(no)
            print("\nFronteira depois da visita:")
            self.printa_fronteira()
            print('-' * 30)

            if compara_nos(no, self.estadoFinal):
                self.formata_saida_solucao_encontrada()

            self.busca_em_profundidade()

    def formata_saida_solucao_encontrada(self):
        print('#' * 30)
        print(str(self.contador_solucao_encontrada) + 'ª SOLUÇÃO ENCONTRADA: ')
        self.printa_nos_visitados(self.contador_solucao_encontrada, self.ordem_de_visita)
        print('#' * 30)
        self.contador_solucao_encontrada += 1
        self.ordem_de_visita = 1

    def coloca_filhos_na_fronteira(self, no):
        for no_filho in no.get_lista_filhos():
            self.fronteira.append(no_filho)

    def verifica_se_estado_final_esta_na_fronteira(self):
        verificacao = False
        for no in self.fronteira:
            if compara_nos(no, self.estadoFinal):
                verificacao = True
        return verificacao


class Movimento:

    def __init__(self, qtd_canibais_no_barco, qtd_missionarios_no_barco):
        self.qtd_canibais_no_barco = qtd_canibais_no_barco
        self.qtd_missionarios_no_barco = qtd_missionarios_no_barco

    def get_canibais_no_barco(self):
        return self.qtd_canibais_no_barco

    def get_missionarios_no_barco(self):
        return self.qtd_missionarios_no_barco
