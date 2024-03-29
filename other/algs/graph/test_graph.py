from unittest import TestCase
from other.algs.graph.graph import SimpleGraph


class TestGraph(TestCase):
    def test_DepthFirstSearch_path_exists(self):
        g = SimpleGraph(4)
        for i in range(g.max_vertex):
            g.AddVertex(i)
        g.AddEdge(0, 1)
        g.AddEdge(0, 2)
        g.AddEdge(1, 2)
        g.AddEdge(2, 3)

        dfs = g.DepthFirstSearch(0, 3)
        self.assertEqual(dfs[0].Value, 0)
        self.assertEqual(dfs[-1].Value, 3)
        self.assertEqual(g.vertex[0], dfs[0])
        self.assertEqual(g.vertex[-1], dfs[-1])

    def test_DepthFirstSearch_path_not_exists(self):
        g = SimpleGraph(4)
        for i in range(g.max_vertex):
            g.AddVertex(i)
        g.AddEdge(0, 1)
        g.AddEdge(0, 2)
        g.AddEdge(1, 2)

        dfs = g.DepthFirstSearch(0, 3)
        self.assertListEqual(dfs, [])

    def test_DepthFirstSearch_path_length_zero(self):
        g = SimpleGraph(4)
        for i in range(g.max_vertex):
            g.AddVertex(i)
        g.AddEdge(0, 1)
        g.AddEdge(0, 2)
        g.AddEdge(1, 2)

        dfs = g.DepthFirstSearch(3, 3)
        self.assertEqual(len(dfs), 1)

    def test_BreadthFirstSearch_path_length_zero(self):
        g = SimpleGraph(4)
        for i in range(g.max_vertex):
            g.AddVertex(i)
        g.AddEdge(0, 1)
        g.AddEdge(0, 2)
        g.AddEdge(1, 2)

        dfs = g.DepthFirstSearch(3, 3)
        self.assertEqual(len(dfs), 1)

    def test_BreadthFirstSearch_path_exists_len_2(self):
        g = SimpleGraph(4)
        for i in range(g.max_vertex):
            g.AddVertex(i)
        g.AddEdge(0, 1)
        g.AddEdge(0, 2)
        g.AddEdge(0, 3)
        g.AddEdge(1, 2)

        bfs = g.BreadthFirstSearch(0, 3)
        self.assertEqual(len(bfs), 2)
        self.assertEqual(g.vertex[0], bfs[0])
        self.assertEqual(g.vertex[-1], bfs[-1])

    def test_BreadthFirstSearch_path_exists_len_3(self):
        g = SimpleGraph(4)
        for i in range(g.max_vertex):
            g.AddVertex(i)
        g.AddEdge(0, 1)
        g.AddEdge(0, 2)
        g.AddEdge(1, 2)
        g.AddEdge(2, 3)

        bfs = g.BreadthFirstSearch(0, 3)
        self.assertEqual(len(bfs), 3)
        self.assertEqual(g.vertex[0], bfs[0])
        self.assertEqual(g.vertex[-1], bfs[-1])

    def test_WeakVertices_3(self):
        g = SimpleGraph(3)
        for i in range(g.max_vertex):
            g.AddVertex(i)
        vs = g.WeakVertices()
        self.assertEqual(len(vs), 3)

    def test_WeakVertices_empty(self):
        g = SimpleGraph(3)
        for i in range(g.max_vertex):
            g.AddVertex(i)
        g.AddEdge(0, 1)
        g.AddEdge(0, 2)
        g.AddEdge(1, 2)

        vs = g.WeakVertices()
        self.assertEqual(len(vs), 0)

    def test_WeakVertices_triangle_with_additional_vertice(self):
        g = SimpleGraph(4)
        for i in range(g.max_vertex):
            g.AddVertex(i)
        g.AddEdge(0, 1)
        g.AddEdge(0, 2)
        g.AddEdge(1, 2)

        vs = g.WeakVertices()
        self.assertEqual(len(vs), 1)

    def test_WeakVertices_butterfly(self):
        g = SimpleGraph(5)
        for i in range(g.max_vertex):
            g.AddVertex(i)
        g.AddEdge(0, 1)
        g.AddEdge(0, 2)
        g.AddEdge(1, 2)
        g.AddEdge(2, 3)
        g.AddEdge(2, 4)
        g.AddEdge(3, 4)

        vs = g.WeakVertices()
        self.assertEqual(len(vs), 0)
