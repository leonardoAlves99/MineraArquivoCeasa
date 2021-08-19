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
    g.nos = set(range(1, 110))
    g.addEdge(1, 54, 45)
    g.addEdge(1, 69, 26)
    g.addEdge(1, 26, 38)
    g.addEdge(1, 62, 36)

    g.addEdge(2, 97, 14)
    g.addEdge(2, 53, 21)
    g.addEdge(2, 98, 28)
    g.addEdge(2, 46, 27)
    g.addEdge(2, 15, 27)
    g.addEdge(2, 10, 11)

    g.addEdge(3, 21, 19)
    g.addEdge(3, 34, 38)
    g.addEdge(3, 25, 34)
    g.addEdge(3, 45, 21)
    g.addEdge(3, 29, 19)
    g.addEdge(3, 94, 40)
    g.addEdge(3, 46, 34)
    g.addEdge(3, 81, 36)

    g.addEdge(4, 53, 45)
    g.addEdge(4, 76, 37)
    g.addEdge(4, 13, 26)
    g.addEdge(4, 18, 28)
    g.addEdge(4, 59, 21)
    g.addEdge(4, 75, 15)
    g.addEdge(4, 83, 12)

    g.addEdge(5, 91, 5)
    g.addEdge(5, 71, 16)
    g.addEdge(5, 47, 35)
    g.addEdge(5, 70, 8)

    g.addEdge(6, 92, 27)
    g.addEdge(6, 52, 5)
    g.addEdge(6, 84, 9)

    g.addEdge(7, 48, 38)
    g.addEdge(7, 37, 23)
    g.addEdge(7, 40, 18)
    g.addEdge(7, 9, 28)
    g.addEdge(7, 100, 42)

    g.addEdge(8, 98, 8)
    g.addEdge(8, 97, 6)

    g.addEdge(9, 68, 54)
    g.addEdge(9, 100, 29)
    g.addEdge(9, 7, 28)

    g.addEdge(10, 2, 11)
    g.addEdge(10, 53, 32)
    g.addEdge(10, 75, 30)
    g.addEdge(10, 92, 21)

    g.addEdge(11, 101, 7)
    g.addEdge(11, 18, 2)
    g.addEdge(11, 59, 11)

    g.addEdge(12, 27, 29)
    g.addEdge(12, 57, 16)
    g.addEdge(12, 28, 30)
    g.addEdge(12, 34, 45)
    g.addEdge(12, 48, 23)

    g.addEdge(13, 102, 15)
    g.addEdge(13, 18, 10)
    g.addEdge(13, 4, 26)

    g.addEdge(14, 60, 12)
    g.addEdge(14, 43, 10)
    g.addEdge(14, 38, 6)

    g.addEdge(15, 2, 27)
    g.addEdge(15, 44, 21)
    g.addEdge(15, 99, 32)
    g.addEdge(15, 92, 37)
    g.addEdge(15, 41, 42)

    g.addEdge(16, 32, 40)
    g.addEdge(16, 45, 14)
    g.addEdge(16, 29, 20)
    g.addEdge(16, 63, 21)
    g.addEdge(16, 81, 32)

    g.addEdge(17, 54, 46)
    g.addEdge(17, 65, 29)
    g.addEdge(17, 51, 35)
    g.addEdge(17, 96, 51)
    g.addEdge(17, 36, 41)

    g.addEdge(18, 13, 10)
    g.addEdge(18, 11, 2)
    g.addEdge(18, 59, 34)
    g.addEdge(18, 4, 28)

    g.addEdge(19, 96, 27)
    g.addEdge(19, 90, 28)
    g.addEdge(19, 61, 26)
    g.addEdge(19, 86, 31)

    g.addEdge(20, 82, 37)
    g.addEdge(20, 102, 23)
    g.addEdge(20, 87, 17)

    g.addEdge(21, 34, 17)
    g.addEdge(21, 98, 19)
    g.addEdge(21, 46, 30)
    g.addEdge(21, 3, 19)

    g.addEdge(22, 33, 8)
    g.addEdge(22, 42, 24)
    g.addEdge(22, 60, 6)

    g.addEdge(23, 47, 10)
    g.addEdge(23, 85, 4)
    g.addEdge(23, 52, 12)

    g.addEdge(24, 99, 11)
    g.addEdge(24, 41, 20)
    g.addEdge(24, 73, 26)
    g.addEdge(24, 30, 23)

    g.addEdge(25, 34, 16)
    g.addEdge(25, 48, 45)
    g.addEdge(25, 40, 37)
    g.addEdge(25, 3, 34)
    g.addEdge(25, 32, 22)

    g.addEdge(26, 1, 38)
    g.addEdge(26, 69, 30)
    g.addEdge(26, 62, 42)

    g.addEdge(27, 86, 25)
    g.addEdge(27, 12, 29)
    g.addEdge(27, 48, 29)

    g.addEdge(28, 57, 14)
    g.addEdge(28, 67, 33)
    g.addEdge(28, 12, 30)
    g.addEdge(28, 34, 32)

    g.addEdge(29, 45, 14)
    g.addEdge(29, 3, 19)
    g.addEdge(29, 16, 20)

    g.addEdge(30, 73, 27)
    g.addEdge(30, 24, 24)
    g.addEdge(30, 74, 21)

    g.addEdge(31, 42, 15)
    g.addEdge(31, 91, 18)
    g.addEdge(31, 56, 16)
    g.addEdge(31, 47, 42)

    g.addEdge(32, 40, 26)
    g.addEdge(32, 25, 22)
    g.addEdge(32, 45, 25)
    g.addEdge(32, 16, 40)
    g.addEdge(32, 100, 34)

    g.addEdge(33, 89, 12)
    g.addEdge(33, 101, 14)
    g.addEdge(33, 22, 8)

    g.addEdge(34, 12, 45)
    g.addEdge(34, 28, 32)
    g.addEdge(34, 98, 42)
    g.addEdge(34, 67, 27)
    g.addEdge(34, 48, 58)
    g.addEdge(34, 25, 16)
    g.addEdge(34, 21, 17)
    g.addEdge(34, 3, 38)

    g.addEdge(35, 44, 62)
    g.addEdge(35, 94, 30)
    g.addEdge(35, 81, 20)
    g.addEdge(35, 73, 15)

    g.addEdge(36, 54, 40)
    g.addEdge(36, 17, 41)
    g.addEdge(36, 96, 39)
    g.addEdge(36, 77, 50)
    g.addEdge(36, 62, 32)

    g.addEdge(37, 7, 23)
    g.addEdge(37, 58, 5)
    g.addEdge(37, 66, 21)

    g.addEdge(38, 14, 6)
    g.addEdge(38, 43, 16)
    g.addEdge(38, 79, 20)
    g.addEdge(38, 50, 12)

    g.addEdge(39, 79, 4)
    g.addEdge(39, 50, 10)
    g.addEdge(39, 80, 11)

    g.addEdge(40, 48, 20)
    g.addEdge(40, 7, 18)
    g.addEdge(40, 25, 37)
    g.addEdge(40, 32, 26)
    g.addEdge(40, 100, 37)

    g.addEdge(41, 15, 42)
    g.addEdge(41, 24, 20)
    g.addEdge(41, 92, 15)
    g.addEdge(41, 84, 12)

    g.addEdge(42, 101, 15)
    g.addEdge(42, 22, 24)
    g.addEdge(42, 55, 10)
    g.addEdge(42, 91, 17)
    g.addEdge(42, 31, 15)

    g.addEdge(43, 60, 15)
    g.addEdge(43, 14, 10)
    g.addEdge(43, 38, 16)
    g.addEdge(43, 79, 6)

    g.addEdge(44, 15, 21)
    g.addEdge(44, 94, 23)
    g.addEdge(44, 35, 62)
    g.addEdge(44, 99, 24)

    g.addEdge(45, 32, 25)
    g.addEdge(45, 16, 28)
    g.addEdge(45, 29, 14)
    g.addEdge(45, 3, 21)

    g.addEdge(46, 2, 27)
    g.addEdge(46, 98, 12)
    g.addEdge(46, 21, 30)
    g.addEdge(46, 3, 34)

    g.addEdge(47, 70, 27)
    g.addEdge(47, 5, 35)
    g.addEdge(47, 31, 42)
    g.addEdge(47, 83, 24)
    g.addEdge(47, 95, 15)
    g.addEdge(47, 85, 14)
    g.addEdge(47, 23, 10)

    g.addEdge(48, 64, 32)
    g.addEdge(48, 27, 29)
    g.addEdge(48, 12, 23)
    g.addEdge(48, 34, 58)
    g.addEdge(48, 25, 45)
    g.addEdge(48, 40, 20)
    g.addEdge(48, 7, 38)

    g.addEdge(49, 67, 39)
    g.addEdge(49, 72, 7)
    g.addEdge(49, 102, 34)
    g.addEdge(49, 97, 12)
    g.addEdge(49, 76, 9)

    g.addEdge(50, 38, 12)
    g.addEdge(50, 79, 8)
    g.addEdge(50, 39, 10)

    g.addEdge(51, 65, 21)
    g.addEdge(51, 17, 35)
    g.addEdge(51, 78, 17)

    g.addEdge(52, 75, 24)
    g.addEdge(52, 23, 12)
    g.addEdge(52, 92, 23)
    g.addEdge(52, 6, 5)

    g.addEdge(53, 97, 16)
    g.addEdge(53, 76, 4)
    g.addEdge(53, 4, 45)
    g.addEdge(53, 2, 21)
    g.addEdge(53, 10, 32)

    g.addEdge(54, 1, 45)
    g.addEdge(54, 17, 46)
    g.addEdge(54, 36, 40)

    g.addEdge(55, 60, 10)
    g.addEdge(55, 79, 16)
    g.addEdge(55, 42, 10)
    g.addEdge(55, 91, 18)
    g.addEdge(55, 71, 7)
    g.addEdge(55, 80, 2)

    g.addEdge(56, 59, 14)
    g.addEdge(56, 31, 16)
    g.addEdge(56, 83, 8)

    g.addEdge(57, 12, 16)
    g.addEdge(57, 28, 14)

    g.addEdge(58, 90, 39)
    g.addEdge(58, 61, 15)
    g.addEdge(58, 64, 45)
    g.addEdge(58, 66, 7)
    g.addEdge(58, 37, 5)

    g.addEdge(59, 11, 11)
    g.addEdge(59, 18, 34)
    g.addEdge(59, 4, 21)
    g.addEdge(59, 56, 14)

    g.addEdge(60, 14, 12)
    g.addEdge(60, 43, 15)
    g.addEdge(60, 55, 10)
    g.addEdge(60, 22, 6)

    g.addEdge(61, 19, 26)
    g.addEdge(61, 64, 21)
    g.addEdge(61, 58, 15)

    g.addEdge(62, 1, 36)
    g.addEdge(62, 26, 42)
    g.addEdge(62, 36, 32)
    g.addEdge(62, 77, 20)

    g.addEdge(63, 100, 52)
    g.addEdge(63, 88, 12)
    g.addEdge(63, 16, 21)
    g.addEdge(63, 81, 9)

    g.addEdge(64, 86, 28)
    g.addEdge(64, 61, 21)
    g.addEdge(64, 58, 45)
    g.addEdge(64, 48, 32)

    g.addEdge(65, 17, 29)
    g.addEdge(65, 51, 21)

    g.addEdge(66, 68, 29)
    g.addEdge(66, 58, 7)
    g.addEdge(66, 37, 21)

    g.addEdge(67, 28, 33)
    g.addEdge(67, 34, 27)
    g.addEdge(67, 97, 44)
    g.addEdge(67, 49, 39)
    g.addEdge(67, 72, 33)
    g.addEdge(67, 82, 26)

    g.addEdge(68, 77, 60)
    g.addEdge(68, 90, 32)
    g.addEdge(68, 66, 29)
    g.addEdge(68, 9, 54)

    g.addEdge(69, 1, 26)
    g.addEdge(69, 26, 30)

    g.addEdge(70, 5, 8)
    g.addEdge(70, 47, 27)

    g.addEdge(71, 55, 7)
    g.addEdge(71, 91, 11)
    g.addEdge(71, 5, 16)
    g.addEdge(71, 93, 5)

    g.addEdge(72, 82, 22)
    g.addEdge(72, 102, 31)
    g.addEdge(72, 67, 33)
    g.addEdge(72, 49, 7)

    g.addEdge(73, 74, 6)
    g.addEdge(73, 30, 27)
    g.addEdge(73, 35, 15)
    g.addEdge(73, 99, 16)
    g.addEdge(73, 24, 26)

    g.addEdge(74, 73, 6)
    g.addEdge(74, 30, 21)

    g.addEdge(75, 95, 12)
    g.addEdge(75, 52, 24)
    g.addEdge(75, 10, 30)
    g.addEdge(75, 4, 15)
    g.addEdge(75, 83, 19)

    g.addEdge(76, 49, 9)
    g.addEdge(76, 53, 4)
    g.addEdge(76, 4, 37)
    g.addEdge(76, 102, 23)

    g.addEdge(77, 62, 20)
    g.addEdge(77, 36, 50)
    g.addEdge(77, 90, 43)
    g.addEdge(77, 68, 60)

    g.addEdge(78, 51, 17)
    g.addEdge(78, 96, 40)
    g.addEdge(78, 86, 20)

    g.addEdge(79, 43, 6)
    g.addEdge(79, 38, 20)
    g.addEdge(79, 50, 8)
    g.addEdge(79, 55, 16)
    g.addEdge(79, 80, 6)
    g.addEdge(79, 39, 4)

    g.addEdge(80, 55, 2)
    g.addEdge(80, 79, 6)
    g.addEdge(80, 39, 11)
    g.addEdge(80, 93, 14)

    g.addEdge(81, 35, 20)
    g.addEdge(81, 88, 23)
    g.addEdge(81, 63, 9)
    g.addEdge(81, 16, 32)
    g.addEdge(81, 94, 47)
    g.addEdge(81, 3, 36)

    g.addEdge(82, 67, 36)
    g.addEdge(82, 72, 22)
    g.addEdge(82, 20, 37)

    g.addEdge(83, 4, 12)
    g.addEdge(83, 56, 8)
    g.addEdge(83, 75, 19)
    g.addEdge(83, 95, 12)
    g.addEdge(83, 47, 24)

    g.addEdge(84, 92, 10)
    g.addEdge(84, 6, 9)
    g.addEdge(84, 41, 12)

    g.addEdge(85, 95, 5)
    g.addEdge(85, 47, 14)
    g.addEdge(85, 23, 4)

    g.addEdge(86, 78, 20)
    g.addEdge(86, 96, 59)
    g.addEdge(86, 19, 31)
    g.addEdge(86, 64, 28)
    g.addEdge(86, 27, 25)

    g.addEdge(87, 20, 17)
    g.addEdge(87, 89, 10)
    g.addEdge(87, 101, 11)

    g.addEdge(88, 100, 43)
    g.addEdge(88, 63, 12)
    g.addEdge(88, 81, 23)

    g.addEdge(89, 87, 10)
    g.addEdge(89, 101, 6)
    g.addEdge(89, 33, 12)

    g.addEdge(90, 77, 43)
    g.addEdge(90, 19, 28)
    g.addEdge(90, 96, 25)
    g.addEdge(90, 58, 39)
    g.addEdge(90, 68, 32)

    g.addEdge(91, 42, 17)
    g.addEdge(91, 55, 18)
    g.addEdge(91, 31, 18)
    g.addEdge(91, 71, 11)
    g.addEdge(91, 5, 5)

    g.addEdge(92, 15, 37)
    g.addEdge(92, 10, 21)
    g.addEdge(92, 99, 41)
    g.addEdge(92, 41, 15)
    g.addEdge(92, 84, 10)
    g.addEdge(92, 6, 27)
    g.addEdge(92, 52, 23)

    g.addEdge(93, 71, 5)
    g.addEdge(93, 80, 14)

    g.addEdge(94, 3, 40)
    g.addEdge(94, 44, 23)
    g.addEdge(94, 81, 47)
    g.addEdge(94, 35, 30)

    g.addEdge(95, 83, 12)
    g.addEdge(95, 47, 15)
    g.addEdge(95, 75, 12)
    g.addEdge(95, 85, 5)

    g.addEdge(96, 36, 39)
    g.addEdge(96, 17, 51)
    g.addEdge(96, 78, 40)
    g.addEdge(96, 86, 59)
    g.addEdge(96, 19, 27)
    g.addEdge(96, 90, 25)

    g.addEdge(97, 67, 44)
    g.addEdge(97, 98, 22)
    g.addEdge(97, 8, 6)
    g.addEdge(97, 49, 12)
    g.addEdge(97, 2, 14)
    g.addEdge(97, 53, 16)

    g.addEdge(98, 8, 8)
    g.addEdge(98, 34, 42)
    g.addEdge(98, 2, 28)
    g.addEdge(98, 97, 22)
    g.addEdge(98, 21, 19)
    g.addEdge(98, 46, 12)

    g.addEdge(99, 44, 24)
    g.addEdge(99, 15, 32)
    g.addEdge(99, 92, 41)
    g.addEdge(99, 24, 11)
    g.addEdge(99, 73, 16)

    g.addEdge(100, 7, 42)
    g.addEdge(100, 9, 29)
    g.addEdge(100, 40, 37)
    g.addEdge(100, 32, 34)
    g.addEdge(100, 63, 52)
    g.addEdge(100, 88, 43)

    g.addEdge(101, 11, 7)
    g.addEdge(101, 87, 11)
    g.addEdge(101, 89, 6)
    g.addEdge(101, 33, 14)
    g.addEdge(101, 42, 15)

    g.addEdge(102, 20, 23)
    g.addEdge(102, 72, 31)
    g.addEdge(102, 49, 34)
    g.addEdge(102, 76, 23)
    g.addEdge(102, 13, 15)

    g.addEdge(103, 20, 23)
    g.addEdge(103, 15, 31)
    g.addEdge(103, 49, 12)
    g.addEdge(103, 69, 23)
    g.addEdge(103, 13, 15)
    g.addEdge(103, 76, 45)
    g.addEdge(103, 37, 78)

    g.addEdge(104, 20, 23)
    g.addEdge(104, 89, 31)
    g.addEdge(104, 49, 34)
    g.addEdge(104, 76, 58)
    g.addEdge(104, 11, 15)

    g.addEdge(105, 20, 46)
    g.addEdge(105, 72, 31)
    g.addEdge(105, 25, 34)

    g.addEdge(106, 20, 23)
    g.addEdge(107, 72, 31)


    g.addEdge(107, 20, 23)
    g.addEdge(107, 92, 31)
    g.addEdge(107, 19, 18)

    g.addEdge(108, 20, 23)
    g.addEdge(108, 72, 58)
    g.addEdge(108, 16, 34)
    g.addEdge(108, 76, 16)

    g.addEdge(109, 46, 23)
    g.addEdge(109, 72, 31)
    g.addEdge(109, 82, 15)

    inicial = 1

    print('Digite o numero do vertice inicial: ')
    inicial=int(input())

    if inicial > 0 and inicial < 110:
        for i in range(1, len(g.nos) + 1):
            if i != inicial:
                print("Caminho do vertice ", inicial, " até o vertice ", i, ": ", shortest_path(g, inicial, i))
    else:
        print('Cidade não encontrada')

# / *Output
#
# SAÍDA DO ALGORITMO
#
#Busca em Profundidade Depth First Search (começando do vértice 1):
# 1):
# 1 - 1
# 2 - 54
# 3 - 17
# 4 - 65
# 5 - 51
# 6 - 78
# 7 - 96
# 8 - 36
# 9 - 77
# 10 - 62
# 11 - 26
# 12 - 69
# 13 - 90
# 14 - 19
# 15 - 61
# 16 - 64
# 17 - 86
# 18 - 27
# 19 - 12
# 20 - 57
# 21 - 28
# 22 - 67
# 23 - 34
# 24 - 98
# 25 - 8
# 26 - 97
# 27 - 49
# 28 - 72
# 29 - 82
# 30 - 20
# 31 - 102
# 32 - 76
# 33 - 53
# 34 - 4
# 35 - 13
# 36 - 18
# 37 - 11
# 38 - 101
# 39 - 87
# 40 - 89
# 41 - 33
# 42 - 22
# 43 - 42
# 44 - 55
# 45 - 60
# 46 - 14
# 47 - 43
# 48 - 38
# 49 - 79
# 50 - 50
# 51 - 39
# 52 - 80
# 53 - 93
# 54 - 71
# 55 - 91
# 56 - 31
# 57 - 56
# 58 - 59
# 59 - 83
# 60 - 75
# 61 - 95
# 62 - 47
# 63 - 70
# 64 - 5
# 65 - 85
# 66 - 23
# 67 - 52
# 68 - 92
# 69 - 15
# 70 - 2
# 71 - 46
# 72 - 21
# 73 - 3
# 74 - 25
# 75 - 48
# 76 - 40
# 77 - 7
# 78 - 37
# 79 - 58
# 80 - 66
# 81 - 68
# 82 - 9
# 83 - 100
# 84 - 32
# 85 - 45
# 86 - 16
# 87 - 29
# 88 - 63
# 89 - 88
# 90 - 81
# 91 - 35
# 92 - 44
# 93 - 94
# 94 - 99
# 95 - 24
# 96 - 41
# 97 - 84
# 98 - 6
# 99 - 73
# 100 - 74
# 101 - 30
# 102 - 10
# * /