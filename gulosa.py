
import heapq


def heuristica(casa, saida):
    # Distância de Manhattan até a saída
    return abs(casa[0] - saida[0]) + abs(casa[1] - saida[1])


def gulosa(grafo, inicio, saida):
    visitados = set()
    fila = []
    anteriores = {inicio: None}

    # A fila prioriza a casa com menor distância estimada
    heapq.heappush(
        fila,
        (heuristica(inicio, saida), inicio)
    )

    while fila:
        _, atual = heapq.heappop(fila)

        # Ignora casas que já foram exploradas
        if atual in visitados:
            continue

        visitados.add(atual)

        # Verifica se chegou à saída
        if atual == saida:
            break

        # Descobre os vizinhos ainda não registrados
        for vizinho in grafo[atual]:
            if vizinho not in anteriores:
                anteriores[vizinho] = atual

                heapq.heappush(
                    fila,
                    (heuristica(vizinho, saida), vizinho)
                )

    # Verifica se a saída foi encontrada
    if saida not in visitados:
        return [], len(visitados)

    # Reconstrói o caminho usando os predecessores
    caminho = []
    atual = saida

    while atual is not None:
        caminho.append(atual)
        atual = anteriores[atual]

    caminho.reverse()

    return caminho, len(visitados)
