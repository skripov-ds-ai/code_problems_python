from unittest import TestCase
from other.algs.queue.queue import Queue


class TestQueue(TestCase):
    def test_size_empty(self):
        q = Queue()
        self.assertEqual(q.size(), 0)

    def test_size_nonempty(self):
        q = Queue()
        for i in range(10):
            q.enqueue(i)
        self.assertEqual(q.size(), 10)

    def test_dequeue_empty(self):
        q = Queue()
        self.assertIsNone(q.dequeue())

    def test_size_after_dequeue(self):
        q = Queue()
        for i in range(10):
            q.enqueue(i)
        self.assertEqual(q.size(), 10)
        for i in range(q.size()):
            q.dequeue()
        self.assertEqual(q.size(), 0)

    # def test_



