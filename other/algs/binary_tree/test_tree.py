from unittest import TestCase
from other.algs.binary_tree.tree import BSTNode, BSTFind, BST


class TestTree(TestCase):
    def make_tree(self):
        pass
        # vals = [1, 2, 3, 5, 5]
        # nodes = []
        # for val in vals:
        #     nodes.append(SimpleTreeNode(val, None))
        # t = SimpleTree(nodes[0])
        # # 1 -> 2
        # t.AddChild(nodes[0], nodes[1])
        # # 1 -> 3
        # t.AddChild(nodes[0], nodes[2])
        # # 2 -> 5
        # t.AddChild(nodes[1], nodes[3])
        # # 2 -> 5
        # t.AddChild(nodes[1], nodes[4])
        # return t, nodes

    def test_Add(self):
        root = BSTNode(5, 5, None)
        # print(type(root))
        t = BST(root)
        # print(type(t.Root))
        t.AddKeyValue(4, 4)
        # print()
        # print(type(t.Root.LeftChild))
        # print(type(t.Root.RightChild))
        # print(type(t.Root))
        self.assertEqual(t.Root.LeftChild.NodeKey, 4)
        t.AddKeyValue(3, 3)
        self.assertEqual(t.Root.LeftChild.LeftChild.NodeKey, 3)
        t.AddKeyValue(6, 6)
        self.assertEqual(t.Root.RightChild.NodeKey, 6)

    def test_Find(self):
        root = BSTNode(5, 5, None)
        t = BST(root)
        t.AddKeyValue(4, 4)
        res = t.FindNodeByKey(5)
        self.assertTrue(res.NodeHasKey)
        self.assertEqual(res.Node, root)

        res = t.FindNodeByKey(4)
        self.assertTrue(res.NodeHasKey)
        self.assertEqual(res.Node, root.LeftChild)

        res = t.FindNodeByKey(3)
        self.assertFalse(res.NodeHasKey)

        t.AddKeyValue(7, 7)
        res = t.FindNodeByKey(7)
        self.assertTrue(res.NodeHasKey)
        self.assertEqual(res.Node, root.RightChild)

    def test_Delete(self):
        root = BSTNode(5, 5, None)
        t = BST(root)
        t.AddKeyValue(4, 4)
        res = t.FindNodeByKey(5)
        self.assertTrue(res.NodeHasKey)
        self.assertEqual(res.Node, root)

        res = t.FindNodeByKey(4)
        self.assertTrue(res.NodeHasKey)
        self.assertEqual(res.Node, root.LeftChild)

        t.DeleteNodeByKey(4)
        res = t.FindNodeByKey(4)
        # print(t.Root.LeftChild.NodeKey)
        self.assertFalse(res.NodeHasKey)





