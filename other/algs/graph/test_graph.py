from unittest import TestCase
from other.algs.graph.graph import SimpleGraph


class TestGraph(TestCase):
    def test_DepthFirstSearch(self):
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
