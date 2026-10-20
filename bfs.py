
from collections import deque


def bfs(grafo, inicio, saida):
    visitados = {inicio}
    fila = deque([inicio])

    # Guarda de onde cada casa foi alcançada
    anteriores = {inicio: None}

    while fila:
        atual = fila.popleft()

        # Verifica se chegou à saída
        if atual == saida:
            break

        # Explora os vizinhos
        for vizinho in grafo[atual]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                anteriores[vizinho] = atual
                fila.append(vizinho)

    # Verifica se a saída foi encontrada
    if saida not in anteriores:
        return [], len(visitados)

    # Reconstrói o caminho da saída até o início
    caminho = []
    atual = saida

    while atual is not None:
        caminho.append(atual)
        atual = anteriores[atual]

    # Inverte para começar pela entrada
    caminho.reverse()

    return caminho, len(visitados)
