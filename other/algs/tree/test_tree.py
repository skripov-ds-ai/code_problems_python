from unittest import TestCase
from other.algs.tree.tree import SimpleTree, SimpleTreeNode


class TestTree(TestCase):
    def make_tree(self):
        vals = [1, 2, 3, 5, 5, 6, 32]
        nodes = []
        for val in vals:
            nodes.append(SimpleTreeNode(val, None))
        t = SimpleTree(nodes[0])
        # 1 -> 2
        t.AddChild(nodes[0], nodes[1])
        # 1 -> 3
        t.AddChild(nodes[0], nodes[2])
        # 2 -> 5
        t.AddChild(nodes[1], nodes[3])
        # 2 -> 5
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

    def test_Count(self):
        t, nodes = self.make_tree()
        t.MoveNode(nodes[1], nodes[2])
        self.assertEqual(len(nodes[2].Children), 1)
        self.assertEqual(t.Count(), len(nodes))

    def test_LeafCount(self):
        t, nodes = self.make_tree()
        t.MoveNode(nodes[1], nodes[2])
        self.assertEqual(len(nodes[2].Children), 1)
        self.assertEqual(t.LeafCount(), 2)

    def test_LeafCount_more(self):
        t, nodes = self.make_tree()
        t.MoveNode(nodes[-1], nodes[1])
        self.assertEqual(t.LeafCount(), 3)

    def test_Even(self):
        t, nodes = self.make_tree()
        t.EvenTrees()
        self.assertEqual(t.LeafCount(), 3)


