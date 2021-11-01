class Grafo(object):

    def __init__(self):
        self.nos = set()
        self.edges = {}
        self.distancia = {}

    def add_no(self, value):
        self.nos.add(value)

    def addEdge(self, from_node, to_node, distance):
        self._add_edge(from_node, to_node, distance)
        self._add_edge(to_node, from_node, distance)

    def _add_edge(self, from_node, to_node, distance):
        self.edges.setdefault(from_node, [])
        self.edges[from_node].append(to_node)
        self.distancia[(from_node, to_node)] = distance

def dijkstra(grafo, no_inicial):
    visitado = {no_inicial: 0}
    current_node = no_inicial
    path = {}

    nos = set(grafo.nos)

    while nos:
        min_node = None
        for node in nos:
            if node in visitado:
                if min_node is None:
                    min_node = node
                elif visitado[node] < visitado[min_node]:
                    min_node = node

        if min_node is None:
            break

        nos.remove(min_node)
        cur_wt = visitado[min_node]

        for edge in grafo.edges[min_node]:
            wt = cur_wt + grafo.distancia[(min_node, edge)]
            if edge not in visitado or wt < visitado[edge]:
                visitado[edge] = wt
                path[edge] = min_node

    return visitado, path

def shortest_path(grafo, no_inicial, goal_node):
    distancia, paths = dijkstra(grafo, no_inicial)
    route = [goal_node]

    while goal_node != no_inicial:
        route.append(paths[goal_node])
        goal_node = paths[goal_node]

    route.reverse()
    return route

if __name__ == '__main__':
    g = Grafo()
    g.nos = set(range(1, 28))
    g.addEdge(1, 2, 1)
    g.addEdge(1, 3, 1)

    g.addEdge(2, 1, 1)
    g.addEdge(2, 3, 1)
    g.addEdge(2, 5, 1)

    g.addEdge(3, 1, 1)
    g.addEdge(3, 2, 1)
    g.addEdge(3, 4, 1)

    g.addEdge(4, 3, 1)
    g.addEdge(4, 6, 1)
    g.addEdge(4, 8, 1)

    g.addEdge(5, 2, 1)
    g.addEdge(5, 7, 1)
    g.addEdge(5, 9, 1)

    g.addEdge(6, 4, 1)
    g.addEdge(6, 8, 1)
    g.addEdge(6, 10, 1)

    g.addEdge(7, 5, 1)
    g.addEdge(7, 9, 1)
    g.addEdge(7, 11, 1)

    g.addEdge(8, 4, 1)
    g.addEdge(8, 6, 1)
    g.addEdge(8, 9, 1)

    g.addEdge(9, 5, 1)
    g.addEdge(9, 8, 1)
    g.addEdge(9, 7, 1)

    g.addEdge(10, 6, 1)
    g.addEdge(10, 12, 1)
    g.addEdge(10, 14, 1)

    g.addEdge(11, 7, 1)
    g.addEdge(11, 13, 1)
    g.addEdge(11, 15, 1)

    g.addEdge(12, 10, 1)
    g.addEdge(12, 14, 1)
    g.addEdge(12, 16, 1)

    g.addEdge(13, 14, 1)
    g.addEdge(13, 15, 1)
    g.addEdge(13, 17, 1)

    g.addEdge(14, 10, 1)
    g.addEdge(14, 12, 1)
    g.addEdge(14, 18, 1)

    g.addEdge(15, 14, 1)
    g.addEdge(15, 13, 1)
    g.addEdge(15, 19, 1)

    g.addEdge(16, 12, 1)
    g.addEdge(16, 22, 1)
    g.addEdge(16, 20, 1)

    g.addEdge(17, 13, 1)
    g.addEdge(17, 23, 1)
    g.addEdge(17, 22, 1)

    g.addEdge(18, 14, 1)
    g.addEdge(18, 24, 1)
    g.addEdge(18, 26, 1)

    g.addEdge(19, 15, 1)
    g.addEdge(19, 25, 1)
    g.addEdge(19, 27, 1)

    g.addEdge(20, 16, 1)
    g.addEdge(20, 22, 1)

    g.addEdge(21, 17, 1)
    g.addEdge(21, 23, 1)

    g.addEdge(22, 16, 1)
    g.addEdge(22, 20, 1)
    g.addEdge(22, 24, 1)

    g.addEdge(23, 17, 1)
    g.addEdge(23, 21, 1)
    g.addEdge(23, 25, 1)

    g.addEdge(24, 18, 1)
    g.addEdge(24, 22, 1)
    g.addEdge(24, 26, 1)

    g.addEdge(25, 19, 1)
    g.addEdge(25, 23, 1)
    g.addEdge(25, 27, 1)

    g.addEdge(26, 18, 1)
    g.addEdge(26, 24, 1)
    g.addEdge(26, 27, 1)

    g.addEdge(27, 19, 1)
    g.addEdge(27, 25, 1)
    g.addEdge(27, 26, 1)

    inicial = 1

    print('Digite o numero do vertice inicial: ')
    inicial=int(input())

    if inicial > 0 and inicial < 28:
        for i in range(1, len(g.nos) + 1):
            if i != inicial:
                print("Caminho do vertice ", inicial, " até o vertice ", i, ": ", shortest_path(g, inicial, i))
    else:
        print('Caminho não encontrada')
