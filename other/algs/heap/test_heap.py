from math import log2
from unittest import TestCase
from other.algs.heap.heap import Heap


class TestHeap(TestCase):
    def test_MakeHeap(self):
        arr = [11, 9, 4, 7, 8, 3, 1, 2, 5, 6]
        h = Heap()
        h.MakeHeap(arr, len(arr))
        print(arr)
        print(h.HeapArray)
        self.assertSetEqual(set(arr) | {None}, set(h.HeapArray))

    def test_GetMax(self):
        arr = [11, 9, 4, 7, 8, 3, 1, 2, 5, 6]
        h = Heap()
        h.MakeHeap(arr, len(arr))
        self.assertEqual(arr[0], h.GetMax())

    def test_GetMax(self):
        arr = sorted([11, 9, 4, 7, 8, 3, 1, 2, 5, 6])
        h = Heap()
        h.MakeHeap(arr, len(arr))
        self.assertEqual(max(arr), h.GetMax())
