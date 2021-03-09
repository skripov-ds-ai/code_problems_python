from unittest import TestCase
from other.algs.tree.tree import SimpleTree, SimpleTreeNode


class TestTree(TestCase):
    def make_tree(self):
        vals = [1, 2, 42, 5, 5]
        nodes = []
        for val in vals:
            nodes.append(SimpleTreeNode(val, None))
        t = SimpleTree(nodes[0])
        t.AddChild(nodes[0], nodes[1])
        t.AddChild(nodes[0], nodes[2])
        t.AddChild(nodes[1], nodes[3])
        t.AddChild(nodes[1], nodes[4])
        return t, nodes

    def test_traversal(self):
        t, _ = self.make_tree()
        nodes = t.traversal(t.Root)
        self.assertTrue(nodes[0].Parent.NodeValue == 2)

    def test_FindNodesByValue(self):
        t, nodes = self.make_tree()
        ns = t.FindNodesByValue(5)
        self.assertEqual(len(ns), 2)
        self.assertEqual(ns[0].NodeValue, 5)
        self.assertEqual(ns[1].NodeValue, 5)

    def test_MoveNode(self):
        t, nodes = self.make_tree()
        t.MoveNode(nodes[1], nodes[2])
        self.assertEqual(len(nodes[2].Children), 1)
        self.assertEqual(nodes[1].Children, nodes[2].Children[0].Children)


