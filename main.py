from labirinto import labirinto, achar, montar_grafo, desenhar
from dfs import dfs
from bfs import bfs
from gulosa import gulosa

inicio = achar(labirinto, 'I')
saida = achar(labirinto, 'F')
grafo = montar_grafo(labirinto)

caminho_dfs, visitadas_dfs = dfs(grafo, inicio, saida)

print("Caminho encontrado pela DFS:")
desenhar(labirinto, caminho_dfs)

print("Tamanho do caminho:", len(caminho_dfs))
print("Casas visitadas:", visitadas_dfs)

print()
print()

caminho_bfs, visitadas_bfs = bfs(grafo, inicio, saida)

print("\nCaminho encontrado pela BFS:")
if caminho_bfs:
    desenhar(labirinto, caminho_bfs)
    print("Tamanho do caminho:", len(caminho_bfs))
else:
    print("Nenhum caminho encontrado.")

print("Casas visitadas:", visitadas_bfs)

print()
print()


caminho_gulosa, visitadas_gulosa = gulosa(
    grafo, inicio, saida
)

print("\nCaminho encontrado pela Busca Gulosa:")
if caminho_gulosa:
    desenhar(labirinto, caminho_gulosa)
    print("Tamanho do caminho:", len(caminho_gulosa))
else:
    print("Nenhum caminho encontrado.")

print("Casas visitadas:", visitadas_gulosa)

print("Coordenadas do caminho da Gulosa:")
print(caminho_gulosa)

