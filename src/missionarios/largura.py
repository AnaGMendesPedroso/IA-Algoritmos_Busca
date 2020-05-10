# Acadêmicos:
# - Ana Gabrielly Mendes Pedroso
# - Davidson Denis Ferreira Guimaraes
# - Larissa Fraga Pinto

import time

class Estado():        

    def __init__(self,missionariosEsquerda, missionariosDireita, canibaisEsquerda, canibaisDireita, ladoRio):

        self.missionariosEsquerda = missionariosEsquerda
        self.missionariosDireita = missionariosDireita
        self.canibaisEsquerda = canibaisEsquerda
        self.canibaisDireita = canibaisDireita
        self.ladoRio = ladoRio
        self.pai = None
        self.filhos = []

    def __str__(self):

        return 'Missionarios: {}\t| Missionarios: {}\nCanibais: {}\t| Canibais: {}'.format(self.missionariosEsquerda, self.missionariosDireita, self.canibaisEsquerda, self.canibaisDireita)

    def verificaEstado(self):
   
        if ((self.missionariosEsquerda < 0) or (self.missionariosDireita < 0)):
            return False

        if ((self.canibaisEsquerda < 0) or (self.canibaisDireita < 0)):
            return False

        return ((self.missionariosEsquerda == 0 or self.missionariosEsquerda >= self.canibaisEsquerda) and (self.missionariosDireita == 0 or self.missionariosDireita >= self.canibaisDireita))

    def estadoFinal(self):
        ladoEsquerdo = self.missionariosEsquerda == self.canibaisEsquerda == 0
        ladoDireito = self.missionariosDireita == self.canibaisDireita == 3
        return ladoEsquerdo and ladoDireito

    def geraFilhos(self):

        # Encontra o novo lado do rio
        novoLadoRio = 'dir' if self.ladoRio == 'esq' else 'esq'
        # Gera a lista de possíveis movimentos
        movimentos = [
            {'missionarios': 2, 'canibais': 0},
            {'missionarios': 1, 'canibais': 0},
            {'missionarios': 1, 'canibais': 1},
            {'missionarios': 0, 'canibais': 1},
            {'missionarios': 0, 'canibais': 2},
        ]
        # Gera todos os possíveis estados e armazena apenas os válidos na lista de filhos
        # do estado atual
        for movimento in movimentos:
            if self.ladoRio == 'esq':
                # Se o barco estiver a esquerda do rio, os missionários e canibais saem da
                # margem esquerda do rio e vão para a direita
                missionariosEsquerda = self.missionariosEsquerda - movimento['missionarios']
                missionariosDireita = self.missionariosDireita + movimento['missionarios']
                canibaisEsquerda = self.canibaisEsquerda - movimento['canibais']
                canibaisDireita = self.canibaisDireita + movimento['canibais']
            else:
                # Caso contrário, os missionários e canibais saem da margem direita do rio
                # e vão para a esquerda
                missionariosDireita = self.missionariosDireita - movimento['missionarios']
                missionariosEsquerda = self.missionariosEsquerda + movimento['missionarios']
                canibaisDireita = self.canibaisDireita - movimento['canibais']
                canibaisEsquerda = self.canibaisEsquerda + movimento['canibais']
            # Cria o estado do filho e caso este seja válido, o adiciona à lista de filhos do pai
            filho = Estado(missionariosEsquerda, missionariosDireita, canibaisEsquerda, canibaisDireita, novoLadoRio)
            filho.pai = self
            if filho.verificaEstado():
                self.filhos.append(filho)

class Missionarios_Canibais():

    def __init__(self):
       
        self.fila_execucao = [Estado(3, 0, 3, 0, 'esq')]
        self.solucao = None

    def geraSolucao(self):

        # Realiza a busca em largura em busca da solução
        for elemento in self.fila_execucao:   
                     
            if elemento.estadoFinal():
                # Se a solução foi encontrada, o caminho que compõe a solução é gerado realizando
                # o caminho de volta até a raiz da árvore de estados e então encerra a busca
                self.solucao = [elemento]
                while elemento.pai:
                    self.solucao.insert(0, elemento.pai)
                    elemento = elemento.pai
                break
            # Caso o elemento não seja a solução, gera seus filhos e os adiciona na fila de execução
            elemento.geraFilhos()
            self.fila_execucao.extend(elemento.filhos)


def main():
    # Instancia o problema e gera sua solução
    problema = Missionarios_Canibais()
    problema.geraSolucao()
    # Exibe a solução em tela, separando cada passo
    for estado in problema.solucao:
        print(estado)
        print(34 * '-')

if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s segundos ---" % (time.time() - start_time))