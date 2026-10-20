# Labirinto - Estrutura de Dados II

## 1. Sobre o projeto

Este trabalho foi desenvolvido para a disciplina de Algoritmos e Estruturas de Dados II. O objetivo é encontrar a saída de um labirinto utilizando três algoritmos de busca: DFS, BFS e Busca Gulosa.


## 2. Como funciona o labirinto

O labirinto foi criado em Python usando uma lista de strings, com 10 linhas e 10 colunas.

Os símbolos utilizados são:

- `I`: início da busca.
- `F`: saída do labirinto.
- `#`: parede, que bloqueia a passagem.
- `.`: casa livre, por onde os algoritmos podem passar.
- `*`: representa o caminho encontrado na visualização.

A função `montar_grafo()` transforma as casas livres em vértices conectados aos seus vizinhos. Os movimentos são verificados na ordem: cima, direita, baixo e esquerda.

A função `achar()` identifica as coordenadas do início e da saída, e a função `desenhar()` mostra o caminho encontrado no terminal.

O labirinto possui rotas alternativas e becos sem saída, permitindo comparar o comportamento dos três algoritmos.

## 3. Algoritmos implementados

### DFS — Busca em Profundidade

A DFS escolhe um caminho e avança o máximo possível. Quando não consegue continuar, volta para tentar outra possibilidade.

Utiliza a recursão como uma pilha para controlar o caminho percorrido. Não garante o menor caminho, pois pode encontrar a saída por uma rota mais longa.

### BFS — Busca em Largura

A BFS explora o labirinto por camadas, começando pelas casas mais próximas do início.

Utiliza uma fila, em que a primeira casa adicionada é a primeira a ser analisada. Como todos os movimentos possuem o mesmo custo, garante um dos menores caminhos possíveis até a saída.

Apesar disso, pode precisar visitar mais casas durante a busca.

### Busca Gulosa

A busca gulosa utiliza uma heurística para estimar a distância entre cada casa e a saída. Neste projeto, foi utilizada a distância de Manhattan, calculada pelas diferenças entre as coordenadas.

O algoritmo prioriza a casa com a menor distância estimada. Como a heurística não considera as paredes, pode escolher uma direção aparentemente melhor, mas que exige desvios. Por isso, não garante o menor caminho.

## 4. Reconstrução dos caminhos

Os três algoritmos retornam o caminho encontrado e a quantidade de casas visitadas.

Na DFS, o caminho é construído durante a exploração, adicionando as casas percorridas e removendo-as quando é necessário voltar.

Na BFS e na Gulosa, o programa registra de qual casa cada posição foi alcançada. Quando encontra a saída, utiliza essas informações para reconstruir o caminho desde o final até o início.

Depois, a função `desenhar()` exibe o resultado de cada algoritmo no terminal.

## 5. Comparação dos resultados

Nos testes realizados com o labirinto desenvolvido, foram obtidos os seguintes resultados:

| Algoritmo | Casas no caminho | Casas visitadas |
|---|---:|---:|
| DFS | 21 | 37 |
| BFS | 19 | 63 |
| Gulosa | 21 | 32 |

Neste projeto, o tamanho do caminho considera as casas desde o início até a saída, incluindo os dois pontos.

A BFS encontrou o menor caminho, com 19 casas, mas visitou mais posições durante a busca. A DFS encontrou um caminho com 21 casas e visitou 37 posições. Já a Gulosa encontrou um caminho com 21 casas, visitando apenas 32 posições.

Os resultados mostram que visitar menos casas não significa necessariamente encontrar o menor caminho.

## 6. Conclusão

O desenvolvimento permitiu comparar três formas diferentes de buscar uma saída em um labirinto.

A DFS explora um caminho em profundidade; a BFS prioriza as casas mais próximas do início e garante o menor caminho em grafos sem pesos; e a Gulosa utiliza uma estimativa de distância até a saída para orientar a busca.

Os testes demonstraram que cada algoritmo possui características diferentes e que a escolha depende do objetivo: encontrar o menor caminho ou reduzir a quantidade de casas exploradas.

## 7. Como executar

É necessário ter o Python instalado.

Com os arquivos do projeto na mesma pasta, execute no terminal:

```bash
python main.py
```

O programa executará os três algoritmos, exibirá os caminhos encontrados e apresentará os resultados para comparação.

## 8. Estrutura do projeto

```text
labirinto_Estrutura_dados_II/
├── main.py
├── labirinto.py
├── dfs.py
├── bfs.py
├── gulosa.py
└── README.md
```

- `main.py`: executa os algoritmos e apresenta os resultados.
- `labirinto.py`: define o labirinto, as direções, a construção do grafo e a visualização.
- `dfs.py`: implementa a busca em profundidade.
- `bfs.py`: implementa a busca em largura.
- `gulosa.py`: implementa a busca gulosa.
- `README.md`: apresenta a descrição e os resultados do trabalho.