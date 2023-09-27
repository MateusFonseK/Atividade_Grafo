class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.matrix = [[0] * num_vertices for _ in range(num_vertices)]
        self.list = [[] for _ in range(num_vertices)]

    def add_edge(self, u, v):
        if 0 <= u < self.num_vertices and 0 <= v < self.num_vertices:
            self.matrix[u][v] = 1
            self.matrix[v][u] = 1
            self.list[u].append(v)
            self.list[v].append(u)

    def print_graph(self):
        print("Matriz de Adjacência:")
        for row in self.matrix:
            print(row)
        
        print("\nLista de Adjacência:")
        for vertex, neighbors in enumerate(self.list):
            print(f"Vértice {vertex}: {neighbors}")

    def dfs(self, start_vertex):
        visited = set()
        stack = []

        stack.append(start_vertex)

        while stack:
            vertex = stack.pop()

            if vertex not in visited:
                print(vertex, end=' ')
                visited.add(vertex)
              
            for neighbor in reversed(self.list[vertex]):
                if neighbor not in visited:
                    stack.append(neighbor)