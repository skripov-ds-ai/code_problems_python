from unittest import TestCase
from other.algs.abst.bbst_array import GenerateBBSTArray


class TestTree(TestCase):
    def test_balancing_small(self):
        arr = [42]
        res = GenerateBBSTArray(arr)
        self.assertEqual(len(res), len(arr))

    def test_balancing_balanced(self):
        arr = [42, 1, 43]
        res = GenerateBBSTArray(arr)
        self.assertEqual(len(arr), len(res))
        self.assertListEqual(arr, res)

    def test_balancing_unbalanced(self):
        arr = [1, 42, 43]
        res = GenerateBBSTArray(arr)
        self.assertEqual(len(arr), len(res))
        self.assertListEqual(res, [42, 1, 43])
