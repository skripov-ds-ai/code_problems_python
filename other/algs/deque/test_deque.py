from unittest import TestCase
from other.algs.deque.deque import Deque


class TestDeque(TestCase):
    def test_size_empty(self):
        q = Deque()
        self.assertEqual(q.size(), 0)

    def test_size_nonempty(self):
        q = Deque()
        for i in range(10):
            q.addTail(i)
        self.assertEqual(q.size(), 10)

    def test_removing_empty(self):
        q = Deque()
        self.assertIsNone(q.removeFront())
        self.assertIsNone(q.removeTail())

    def test_size_after_remove_tail(self):
        q = Deque()
        for i in range(10):
            q.addTail(i)
        self.assertEqual(q.size(), 10)
        for i in range(q.size()):
            q.removeTail()
        self.assertEqual(q.size(), 0)

    def test_insert_front(self):
        q = Deque()
        q.addFront(42)
        q.addFront(0)
        item = q.removeFront()
        self.assertEqual(item, 0)

    def test_insert_tail(self):
        q = Deque()
        q.addTail(42)
        q.addTail(0)
        item = q.removeTail()
        self.assertEqual(item, 0)

    def test_remove_head_after_insert_tail(self):
        q = Deque()
        q.addTail(35)
        q.addTail(37)
        item = q.removeFront()
        self.assertEqual(item, 35)

    # def test_



