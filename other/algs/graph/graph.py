class Vertex:
    def __init__(self, val):
        self.Value = val
        self.Hit = False


class SimpleGraph:
    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size

    def AddVertex(self, v):
        # ваш код добавления новой вершины
        # с значением value
        # в свободное место массива vertex
        for i in range(self.max_vertex):
            if self.vertex[i] is None:
                self.vertex[i] = Vertex(v)
                break

    # здесь и далее, параметры v -- индекс вершины
    # в списке  vertex
    def RemoveVertex(self, v):
        # ваш код удаления вершины со всеми её рёбрами
        self.vertex[v] = None
        for i in range(self.max_vertex):
            self.m_adjacency[i][v] = 0
            self.m_adjacency[v][i] = 0

    def IsEdge(self, v1, v2):
        # True если есть ребро между вершинами v1 и v2
        return self.m_adjacency[v1][v2] == 1 and self.m_adjacency[v2][v1] == 1

    def AddEdge(self, v1, v2):
        # добавление ребра между вершинами v1 и v2
        self.m_adjacency[v1][v2] = 1
        self.m_adjacency[v2][v1] = 1

    def RemoveEdge(self, v1, v2):
        # удаление ребра между вершинами v1 и v2
        self.m_adjacency[v1][v2] = 0
        self.m_adjacency[v2][v1] = 0

    def DepthFirstSearch(self, VFrom, VTo):
        # узлы задаются позициями в списке vertex
        # возвращается список узлов -- путь из VFrom в VTo
        # или [] если пути нету
        if VFrom < 0 or VFrom > len(self.vertex) or VTo < 0 or VTo > len(self.vertex):
            return []
        if self.vertex[VFrom] is None or self.vertex[VTo] is None:
            return []
        if VFrom == VTo:
            return [self.vertex[VTo]]
        stack = [VFrom]
        for v in self.vertex:
            v.Hit = False
        self.vertex[VFrom].Hit = True

        while stack:
            v = stack[-1]
            self.vertex[v].Hit = True

            if self.m_adjacency[v][VTo]:
                self.vertex[VTo].Hit = True
                stack.append(VTo)
                break
            all_visited = True
            for i in range(self.max_vertex):
                if v != i and self.m_adjacency[v][i]:
                    all_visited = all_visited and self.vertex[i].Hit
            if all_visited:
                stack.pop()
            else:
                for i in range(self.max_vertex):
                    if v != i and self.m_adjacency[v][i] and not self.vertex[i].Hit:
                        stack.append(i)
                        break

        if not stack or stack and stack[-1] != VTo:
            return []

        result = []
        for i in stack:
            result.append(self.vertex[i])
        return result
