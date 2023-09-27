import queue

class Graph:
  def __init__(self, num_vert):
    self.num_vertices = num_vert
    self.matix = [[0 for _ in range(num_vert)] for _ in range(num_vert)]
    self.list = [[] for _ in range(num_vert)]


  def print(self):
    print(f"\n{self.matix}\n")
    print(f"\n{self.list}\n")

  def bfs(self, source):
    fila = queue.Queue()
    fila.put(source)

    dist = [-1 for _ in range(self.num_vertices)]
    ant = [-1 for _ in range(self.num_vertices)]
    isVisited = [False for _ in range(self.num_vertices)]
    isVisited[source] = True
    dist[source] = 0

    while fila.empty() != True:
      p = fila.get()

      for v in self.list[p]:
        if (isVisited[v] == False):
          dist[v] = dist[p] + 1
          ant[v] = p
          fila.put(v)
          isVisited[v] = True

    return dist, ant 
    
  def print_path(self, s, t, ant):
    if ant[t] == -1:
      print("Não há caminho entre os vértices.")
      return
      
    path = []
    
    while t != s:
        
      path.append(t)
      t = ant[t]

    path.append(s)
    path.reverse()

    print("\nCaminho entre os vértices:")
    print(" -> ".join(map(str, path)))