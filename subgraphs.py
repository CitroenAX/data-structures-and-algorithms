# subgraphs.py


class Graph:
    def __init__(self, n):
        self.n = n
        self.neighbors = []

        for vertex in range(n):
            self.neighbors.append([])

    def add(self, u, v):
        if v not in self.neighbors[u]:
            self.neighbors[u].append(v)

        if u != v and u not in self.neighbors[v]:
            self.neighbors[v].append(u)

    def remove(self, u, v):
        if v in self.neighbors[u]:
            self.neighbors[u].remove(v)

        if u != v and u in self.neighbors[v]:
            self.neighbors[v].remove(u)

    def subgraphs(self):
        visited = []
        for vertex in range(self.n):
            visited.append(False)

        component_count = 0

        for start_vertex in range(self.n):
            if visited[start_vertex]:
                continue

            component_count += 1
            stack = [start_vertex]
            visited[start_vertex] = True

            while len(stack) > 0:
                current_vertex = stack.pop()

                for neighbor in self.neighbors[current_vertex]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)

        return component_count


if __name__ == "__main__":
    graph = Graph(6)

    edges = ((0, 4), (2, 1), (2, 5), (3, 0), (5, 1))
    for u, v in edges:
        graph.add(u, v)

    print(graph.subgraphs())

    more_edges = ((0, 2), (2, 3), (3, 5), (4, 5))
    for u, v in more_edges:
        graph.add(u, v)

    print(graph.subgraphs())