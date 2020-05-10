# Acadêmicos:
# - Ana Gabrielly Mendes Pedroso
# - Davidson Denis Ferreira Guimaraes
# - Larissa Fraga Pinto


import src.potes_dfs.dfs

from datetime import datetime

pote5 = src.potes_dfs.dfs.Pote(0,5)
pote7 = src.potes_dfs.dfs.Pote(0,7)
no_inicial = src.potes_dfs.dfs.No(pote5,pote7)
grafo = src.potes_dfs.dfs.Grafo(no_inicial)
grafo.gerar_grafo()
dfs = src.potes_dfs.dfs.DFS(grafo.get_lista_nos_grafo(), no_inicial)

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
