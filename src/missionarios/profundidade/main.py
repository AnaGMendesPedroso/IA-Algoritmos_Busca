# Academicos:
# - Ana Gabrielly Mendes Pedroso
# - Davidson Denis Ferreira Guimaraes
# - Larissa Fraga Pinto


import src.missionarios.profundidade.profundidade

from datetime import datetime


movimentos_validos = []
mov1 = src.missionarios.profundidade.profundidade.Movimento(1, 0)
mov2 = src.missionarios.profundidade.profundidade.Movimento(2, 0)
mov3 = src.missionarios.profundidade.profundidade.Movimento(0, 1)
mov4 = src.missionarios.profundidade.profundidade.Movimento(0, 2)
mov5 = src.missionarios.profundidade.profundidade.Movimento(1, 1)

movimentos_validos.append(mov1)
movimentos_validos.append(mov2)
movimentos_validos.append(mov3)
movimentos_validos.append(mov4)
movimentos_validos.append(mov5)

no_inicial = src.missionarios.profundidade.profundidade.No(3, 3, 1)
no_final = src.missionarios.profundidade.profundidade.No(0, 0, 0)
grafo = src.missionarios.profundidade.profundidade.Grafo(no_inicial, no_final, movimentos_validos)
grafo.gerar_grafo()
dfs = src.missionarios.profundidade.profundidade.DFS(grafo.get_lista_nos_grafo(), no_inicial, no_final)

inicio = datetime.now()
dfs.busca_em_profundidade()
fim = datetime.now()

inicio_execucao_hora = inicio.hour
inicio_execucao_minuto = inicio.minute
inicio_execucao_segundo = inicio.second
inicio_execucao_microsegundo = inicio.microsecond

fim_execucao_hora = fim.hour
fim_execucao_minuto = fim.minute
fim_execucao_segundo = fim.second
fim_execucao_microsegundo = fim.microsecond

print("Início da execução = %d:%d:%d:%d" % (inicio_execucao_hora, inicio_execucao_minuto, inicio_execucao_segundo, inicio_execucao_microsegundo))
print("Fim da execução = %d:%d:%d:%d" % (fim_execucao_hora, fim_execucao_minuto, fim_execucao_segundo, fim_execucao_microsegundo))

diferenca_hora = fim_execucao_hora - inicio_execucao_hora
diferenca_minuto = fim_execucao_minuto - inicio_execucao_minuto
diferenca_segundo = fim_execucao_segundo - inicio_execucao_segundo
diferenca_microsegundo = fim_execucao_microsegundo - inicio_execucao_microsegundo

print("Tempo de execução DFS:  %d:%d:%d:%d" %(diferenca_hora, diferenca_minuto, diferenca_segundo, diferenca_microsegundo))
print("Número de estados expandidos: "+ str(len(dfs.nos_visitados)))