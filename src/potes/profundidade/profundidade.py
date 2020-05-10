# Acadêmicos:
# - Ana Gabrielly Mendes Pedroso
# - Davidson Denis Ferreira Guimaraes
# - Larissa Fraga Pinto


def formata_saida(no):    
    return '[' + str(no.pote_cinco.conteudo) + ',' + str(no.pote_sete.conteudo) + ']'

def compara_nos(no1, no2):
    comparacao = False
    if no1.pote_cinco.conteudo == no2.pote_cinco.conteudo \
            and no1.pote_sete.conteudo == no2.pote_sete.conteudo:
        comparacao = True
    return comparacao

def encher(pote):
    novo_pote = None
    if pote.conteudo < pote.capacidade_max:
        if pote.capacidade_max == 5:
            novo_pote = Pote(5, 5)
        elif pote.capacidade_max == 7:
            novo_pote = Pote(7, 7)
    return novo_pote

def esvaziar(pote):
    novo_pote = None
    if pote.conteudo > 0:
        novo_pote = Pote(0, pote.capacidade_max)
    return novo_pote


def verter(origem, destino):
    vet_potes = []
    novo_pote_origem = None
    novo_pote_destino = None
    if origem.conteudo != 0 and destino.conteudo + origem.conteudo <= destino.capacidade_max:
        novo_pote_destino = Pote((destino.conteudo + origem.conteudo), destino.capacidade_max)
        novo_pote_origem = Pote(0, origem.capacidade_max)

        vet_potes.append(novo_pote_origem)
        vet_potes.append(novo_pote_destino)

    return vet_potes

class Pote:
    def __init__(self, conteudo, capacidade_Max):
        self.conteudo = conteudo
        self.capacidade_max = capacidade_Max
    
    
class No:

    def __init__(self, pote_cinco, pote_sete):
        self.pote_cinco = pote_cinco
        self.pote_sete = pote_sete
        self.lista_filhos = []
        self.lista_pais = []

class Grafo:

    def __init__(self, noInicial):
        self.noInicial = noInicial
        self.nos_grafo = []
        self.nos_grafo.append(noInicial)

    def get_lista_nos_grafo(self):
        return self.nos_grafo

    def verifica_no_ja_inserido(self, no):
        verifica = False
        for no_inserido in self.nos_grafo:
            if compara_nos(no, no_inserido):
                verifica = no_inserido
                break
        return verifica

    def gerar_grafo(self):
        for no in self.nos_grafo:
            self.gerar_nos_filhos(no)
            for filho in no.lista_filhos:
                self.nos_grafo.append(filho)

        print('Estados do grafo gerado')
        for no in self.nos_grafo:
            print(formata_saida(no))
        print('='*30)

    def gerar_nos_filhos(self, no_pai):
        if not esvaziar(no_pai.pote_cinco) is None:
            filho = No(esvaziar(no_pai.pote_cinco), no_pai.pote_sete)
            self.valida_e_insere(filho, no_pai)

        if not esvaziar(no_pai.pote_sete) is None:
            filho = No(no_pai.pote_cinco, esvaziar(no_pai.pote_sete))
            self.valida_e_insere(filho, no_pai)

        if not encher(no_pai.pote_cinco) is None:
            filho = No(encher(no_pai.pote_cinco), no_pai.pote_sete)
            self.valida_e_insere(filho, no_pai)

        if not encher(no_pai.pote_sete) is None:
            filho = No(no_pai.pote_cinco, encher(no_pai.pote_sete))
            self.valida_e_insere(filho, no_pai)

        if len(verter(no_pai.pote_cinco, no_pai.pote_sete)) > 0:
            nos_verter = verter(no_pai.pote_cinco, no_pai.pote_sete)
            pot5 = nos_verter.pop(0)
            pot7 = nos_verter.pop(1)
            filho = No(pot5, pot7)
            self.valida_e_insere(filho, no_pai)

        if len(verter(no_pai.pote_sete, no_pai.pote_cinco)) > 0:
            nos_verter = verter(no_pai.pote_sete, no_pai.pote_cinco)
            pot5 = nos_verter.pop(1)
            pot7 = nos_verter.pop(0)
            filho = No(pot5, pot7)
            self.valida_e_insere(filho, no_pai)

    def valida_e_insere(self, filho, no_pai):
        old = self.verifica_no_ja_inserido(filho)
        if not old:
            no_pai.lista_filhos.append(filho)
            filho.lista_pais.append(no_pai)
        else:
            no_pai.lista_filhos.append(old)
            old.lista_pais.append(no_pai)


class DFS:

    def __init__(self, grafo, no_inicial):
        self.candidados = []
        self.nos_visitados = []
        self.pais = dict
        self.no_inicial = no_inicial
        self.grafo = grafo
        self.candidados.append(no_inicial)

    def printa_nos_visitados(self):
        for no in self.nos_visitados:
            print(formata_saida(no))

    def printa_candidados(self):
        for no in self.candidados:
            print(formata_saida(no))

    def busca_em_profundidade(self):
        if len(self.candidados) > 0:
            no = self.candidados.pop()
            self.pais = no
            print("\nNó que será visitado:")
            print(formata_saida(no))
            print("\nCandidados antes da visita:")
            self.printa_candidados()
            self.nos_visitados.append(no)
            self.coloca_filhos_como_candidados(no)
            print("\nCandidados depois da visita:")
            self.printa_candidados()
            print('-' * 30)

            if self.verifica_estado_final_como_candidato():
                self.formata_saida_solucao_encontrada(no)

            self.busca_em_profundidade()

    def verifica_estado_final_como_candidato(self):
        comparacao = False
        for no in self.candidados:
            if no.pote_cinco.conteudo == 4 or no.pote_sete.conteudo == 4:
                comparacao = True
                break
        return comparacao

    def coloca_filhos_como_candidados(self, no):
        for no_filho in no.lista_filhos:
            self.candidados.append(no_filho)

    def formata_saida_solucao_encontrada(self):
        print('#' * 30)
        resposta = []
        no = self.pais
        while not compara_nos(no, self.no_inicial):
                resposta.append(no)
                no = self.pais[no]
        resposta.append(self.no_inicial)
        resposta.reverse()
        print('SOLUÇÃO ENCONTRADA: ', resposta)
        print('#' * 30)
