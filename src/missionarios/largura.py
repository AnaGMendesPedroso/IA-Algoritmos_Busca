# Academicos:
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

        return ' {} | {}\n {} | {}'.format(self.missionariosEsquerda, self.missionariosDireita, self.canibaisEsquerda, self.canibaisDireita)

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
        if (self.ladoRio == 'esquerda'):
            novoLadoRio = 'direita'
        else:
            novoLadoRio = 'esquerda'
        
        movimentosPossiveis = [
            {'missionarios': 2, 'canibais': 0},
            {'missionarios': 1, 'canibais': 0},
            {'missionarios': 1, 'canibais': 1},
            {'missionarios': 0, 'canibais': 1},
            {'missionarios': 0, 'canibais': 2},
        ]
        
        for movimento in movimentosPossiveis:
            if (self.ladoRio == 'esquerda'):
                missionariosEsquerda = self.missionariosEsquerda - movimento['missionarios']
                missionariosDireita = self.missionariosDireita + movimento['missionarios']
                canibaisEsquerda = self.canibaisEsquerda - movimento['canibais']
                canibaisDireita = self.canibaisDireita + movimento['canibais']
            else:
                missionariosDireita = self.missionariosDireita - movimento['missionarios']
                missionariosEsquerda = self.missionariosEsquerda + movimento['missionarios']
                canibaisDireita = self.canibaisDireita - movimento['canibais']
                canibaisEsquerda = self.canibaisEsquerda + movimento['canibais']
            # Cria o filho e caso este seja válido, adiciona o filho na lista de filhos do pai
            filho = Estado(missionariosEsquerda, missionariosDireita, canibaisEsquerda, canibaisDireita, novoLadoRio)
            filho.pai = self
            if filho.verificaEstado():
                self.filhos.append(filho)
                print('-------------')
                print('Nó visitado')
                print(filho)
                print('-------------')

class Bfs():

    def __init__(self):
       
        self.filaExecucao = [Estado(3, 0, 3, 0, 'esquerda')]
        self.solucao = None

    def geraSolucao(self):

        # Realiza a busca em largura em busca da solução
        for elemento in self.filaExecucao: 
            print('-------------')  
            print('Caminho da solução')
            print(elemento)
            print('-------------')

            if elemento.estadoFinal():
                # Se foi encontrada a solucao, e gerado o caminho reverso e encerra a busca
                self.solucao = [elemento]
                while elemento.pai:
                    self.solucao.insert(0, elemento.pai)
                    elemento = elemento.pai
                break
            # Caso o elemento ao for a solucao, gera seus filhos e os adiciona na fila de execução
            elemento.geraFilhos()
            self.filaExecucao.extend(elemento.filhos)


def main():
    # Chama o metodo de busca e gera a solucao
    problema = Bfs()
    problema.geraSolucao()
    # Imprime a solucao
    for estado in problema.solucao:
        print(estado)
        print('--------')

if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s segundos ---" % (time.time() - start_time))