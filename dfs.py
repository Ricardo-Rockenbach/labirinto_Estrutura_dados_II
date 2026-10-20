
def dfs(grafo, inicio, saida):
    visitados = set()
    caminho = []

    def buscar(atual):
        visitados.add(atual)
        caminho.append(atual)

        if atual == saida:
            return True

        for vizinho in grafo[atual]:
            if vizinho not in visitados:
                if buscar(vizinho):
                    return True

        caminho.pop()
        return False

    encontrou = buscar(inicio)

    if encontrou:
        return caminho, len(visitados)

    return [], len(visitados)
