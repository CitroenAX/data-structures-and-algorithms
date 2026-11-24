# paths.py


class Graph:
    def __init__(self, n):
        self.n = n
        self.edges = []

        for row in range(n):
            edge_row = []
            for column in range(n):
                edge_row.append(None)
            self.edges.append(edge_row)

    def add(self, u, v, w):
        self.edges[u][v] = w

    def remove(self, u, v):
        self.edges[u][v] = None

    def all_paths(self):
        distances = []

        for row in range(self.n):
            distance_row = []
            for column in range(self.n):
                distance_row.append(self.edges[row][column])
            distances.append(distance_row)

        for vertex in range(self.n):
            if distances[vertex][vertex] is None or distances[vertex][vertex] > 0:
                distances[vertex][vertex] = 0

        for middle in range(self.n):
            for start in range(self.n):
                if distances[start][middle] is None:
                    continue

                for end in range(self.n):
                    if distances[middle][end] is None:
                        continue

                    new_distance = (
                        distances[start][middle] + distances[middle][end]
                    )

                    if distances[start][end] is None:
                        distances[start][end] = new_distance
                    elif new_distance < distances[start][end]:
                        distances[start][end] = new_distance

        for vertex in range(self.n):
            if distances[vertex][vertex] < 0:
                raise ValueError("Graph contains a negative-weight cycle")

        result = []
        for start in range(self.n):
            result_row = []
            for end in range(self.n):
                if distances[start][end] is None:
                    result_row.append(-1)
                else:
                    result_row.append(distances[start][end])
            result.append(result_row)

        return result


if __name__ == "__main__":
    graph = Graph(6)
    edges = ((0, 2, 7), (0, 4, 9), (2, 1, 5),
             (2, 3, 1), (2, 5, 2), (3, 0, 6),
             (3, 5, 2), (4, 5, 1), (5, 1, 6))
    for u, v, w in edges:
        graph.add(u, v, w)

    matrix = graph.all_paths()
    for weights in matrix:
        for weight in weights:
            print(f"{weight:3d}", end="")
        print()