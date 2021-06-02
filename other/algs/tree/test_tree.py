from unittest import TestCase
from other.algs.tree.tree import SimpleTree, SimpleTreeNode


class TestTree(TestCase):
    def make_tree(self):
        vals = [1, 2, 3, 5, 5]
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

    def test_RecursiveCount(self):
        t, nodes = self.make_tree()
        self.assertEqual(t.RecursiveCount(t.Root), len(nodes))
        self.assertEqual(t.RecursiveCount(t.Root.Children[0]), 3)

    def test_Even(self):
        t, nodes = self.make_tree()
        t.EvenTrees()
        self.assertEqual(t.LeafCount(), 3)

    def test_EvenTrees_EmptyTree(self):
        t = SimpleTree(None)
        res = t.EvenTrees()
        self.assertEqual(res, [])

    def test_EvenTrees_Three(self):
        parent = SimpleTreeNode(1, None)
        t = SimpleTree(parent)
        t.AddChild(t.Root, SimpleTreeNode(2, t.Root))
        t.AddChild(t.Root, SimpleTreeNode(3, t.Root))
        t.AddChild(t.Root, SimpleTreeNode(6, t.Root))
        t.AddChild(t.Root.Children[0], SimpleTreeNode(5, t.Root.Children[0]))
        t.AddChild(t.Root.Children[0], SimpleTreeNode(7, t.Root.Children[0]))
        t.AddChild(t.Root.Children[1], SimpleTreeNode(4, t.Root.Children[1]))
        t.AddChild(t.Root.Children[2], SimpleTreeNode(8, t.Root.Children[2]))
        t.AddChild(t.Root.Children[2].Children[0], SimpleTreeNode(9, t.Root.Children[2].Children[0]))
        t.AddChild(t.Root.Children[2].Children[0], SimpleTreeNode(10, t.Root.Children[2].Children[0]))

        res = t.EvenTrees()
        res = [x.NodeValue for x in res]
        self.assertEqual(res, [1, 3, 1, 6])

    def test_EvenTrees_Odd(self):
        parent = SimpleTreeNode(1, None)
        t = SimpleTree(parent)
        t.AddChild(t.Root, SimpleTreeNode(2, t.Root))
        t.AddChild(t.Root, SimpleTreeNode(3, t.Root))
        res = t.EvenTrees()
        self.assertEqual(res, [])
