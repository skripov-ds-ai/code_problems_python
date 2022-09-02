from unittest import TestCase
from other.algs.abst.abst import aBST


class TestTree(TestCase):
    def test_abst_size(self):
        tree = aBST(0)
        self.assertEqual(tree.tree_size, 1)
        tree = aBST(5)
        self.assertEqual(tree.tree_size, 63)
        tree = aBST(2)
        self.assertEqual(tree.tree_size, 7)

    def test_find(self):
        tree = aBST(2)
        tree.AddKey(8)
        tree.AddKey(4)
        tree.AddKey(32)
        expected = [8, 4, 32, None, None, None, None]
        self.assertListEqual(tree.Tree, expected)
        other = [8, 4, 32, 1, 2, 16, 64][3:]
        for o in other:
            tree.AddKey(o)
        self.assertEqual(tree.FindKeyIndex(1024), None)
