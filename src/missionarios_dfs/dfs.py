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
        self.listaNosPais = []
        self.listaNosFilhos = []
        self.solucao_e_ordem_de_visita = []

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

    def set_solucao_ordem_de_visita(self,id_solucao_ordem_da_visita, ordem_de_visita):
        aux = [id_solucao_ordem_da_visita,ordem_de_visita]
        self.solucao_e_ordem_de_visita.append(aux)

    def get_solucao_ordem_visita(self):
        return self.solucao_e_ordem_de_visita

class Grafo:

    def __init__(self, noInicial,noFinal, movimentosPossiveis):
        self.noInicial = noInicial
        self.noFinal = noFinal
        self.movimentosPossiveis = movimentosPossiveis
        self.nos_grafo = []
        self.nos_grafo.append(noInicial)

    def get_lista_nos_grafo(self):
        return self.nos_grafo

    def gerar_grafo(self):
        for no in self.nos_grafo:
            self.gerar_nos_filhos(no)

        print('Estados do grafo gerado')
        for no in self.nos_grafo:
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
        for no_grafo in self.nos_grafo:
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
            self.nos_grafo.append(no_recem_criado)


class DFS:

    def __init__(self, grafo, estadoInicial, estadoFinal):
        self.fronteira = []
        self.nos_visitados = []
        self.estadoInicial = estadoInicial
        self.estadoFinal = estadoFinal
        self.grafo = grafo
        self.solucao_atual = 1
        self.ordem_de_visita = 1
        self.fronteira.append(estadoInicial)

    def printa_nos_visitados(self):
        ordem = 1
        for no in self.nos_visitados:
            for solucao in no.get_solucao_ordem_visita():
                if self.solucao_atual == solucao[0] and ordem == solucao[1]:
                    print(formata_saida(no))
                    ordem += 1

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
            no.set_solucao_ordem_de_visita(self.solucao_atual, self.ordem_de_visita)
            self.ordem_de_visita += 1
            self.coloca_filhos_na_fronteira(no)
            print("\nFronteira depois da visita:")
            self.printa_fronteira()
            print('-' * 30)

            if compara_nos(no, self.estadoFinal):
                self.formata_saida_solucao_encontrada(no)

            self.busca_em_profundidade()

    def coloca_filhos_na_fronteira(self, no):
        for no_filho in no.get_lista_filhos():
            self.fronteira.append(no_filho)

    def formata_saida_solucao_encontrada(self, no_disparo):
        print('#' * 30)
        print(str(self.solucao_atual) +'ª SOLUÇÃO ENCONTRADA: ')
        self.printa_nos_visitados()
        self.solucao_atual += 1
        self.adiciona_solucao_atual_a_todos_nos_visitados(no_disparo)
        self.ordem_de_visita = 1
        print('#' * 30)

    def adiciona_solucao_atual_a_todos_nos_visitados(self, no_disparo):
        for no in self.nos_visitados:
            primeira_solucao_no = no.get_solucao_ordem_visita()[0]
            irmaos = self.get_irmaos_estao_na_fronteira(no)
            irmao_disparou_solucao = False
            for no_irmao in irmaos:
                if compara_nos(no_disparo,no_irmao):
                    irmao_disparou_solucao = True
                    break

            if len(irmaos) == 0 or not irmao_disparou_solucao:
                no.set_solucao_ordem_de_visita(self.solucao_atual, primeira_solucao_no[1])

    def get_irmaos_estao_na_fronteira(self, no):
        irmaos = []
        for pai in no.get_lista_pais():
            for filho_desse_pai in pai.get_lista_filhos():
                if not compara_nos(filho_desse_pai, no) and self.verifica_se_estado_esta_na_fronteira(filho_desse_pai):
                    irmaos.append(filho_desse_pai)

        return irmaos

    def verifica_se_estado_esta_na_fronteira(self,estado_comparacao):
        verificacao = False
        for no in self.fronteira:
            if compara_nos(no, estado_comparacao):
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