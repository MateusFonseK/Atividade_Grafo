from Graph_DFS import Graph


def load_graph(fileName):
  file = open(fileName, 'r')
  num_vert = int(file.readline())

  graph = Graph(num_vert)

  linha = 0
  for line in file:
    line.strip()
    numeros = line.split("\t")
    coluna = 0
    for i in numeros:
      if (coluna == graph.num_vertices):
        break

      graph.matrix[linha][coluna] = int(i)
      if (graph.matrix[linha][coluna] > 0):
        graph.list[linha].append(coluna)

      coluna += 1

    linha += 1

  return graph

# exemplo pcv4
gr = load_graph("pcv4.txt")

# DFS a partir do vértice escolhido
start_vertex = 3
print(f"DFS a partir do vértice {start_vertex}:")
gr.dfs(start_vertex)