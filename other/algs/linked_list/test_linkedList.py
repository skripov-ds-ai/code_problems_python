from unittest import TestCase
from other.algs.linked_list.linked_list import LinkedList, Node


class TestLinkedList(TestCase):
    def make_list(self, *vals):
        l = LinkedList()
        nodes = []
        for v in vals:
            node = Node(v)
            l.add_in_tail(node)
            nodes.append(node)
        return l, nodes

    def test_find_all(self):
        selected = 1
        l, nodes = self.make_list(1, 1, 1, 42, 1)
        nodes = [node for node in nodes if node.value == selected]
        found = l.find_all(selected)
        self.assertListEqual(nodes, found)

    def test_delete_first(self):
        selected = 1
        l, _ = self.make_list(2, 2, 2, 42, 1)
        size = l.len() - 1
        l.delete(selected, all=False)
        self.assertEqual(size, l.len())

    def test_delete_first_empty(self):
        selected = 1
        l, _ = self.make_list()
        size = 0
        l.delete(selected, all=False)
        self.assertEqual(size, l.len())

    def test_delete_first_one_element(self):
        selected = 1
        l, _ = self.make_list(1)
        size = 0
        l.delete(selected, all=False)
        self.assertEqual(size, l.len())

    def test_delete_all(self):
        selected = 1
        l, _ = self.make_list(1, 1, 2, 1, 42, 1, 42, 42)
        size = l.len() - 4
        l.delete(selected, all=True)
        self.assertEqual(size, l.len())

    def test_clean(self):
        l, _ = self.make_list(1, 2)
        l.clean()
        self.assertEqual(0, l.len())

    def test_len_empty(self):
        l, _ = self.make_list()
        self.assertEqual(0, l.len())

    def test_len_non_empty(self):
        l, _ = self.make_list(1, 2, 42)
        self.assertEqual(3, l.len())

    def test_insert_start(self):
        l, _ = self.make_list()
        self.assertEqual(0, l.len())
        node = Node(42)
        l.insert(None, node)
        self.assertEqual(1, l.len())
        self.assertEqual(42, l.head.value)

    def test_insert_after(self):
        l, nodes = self.make_list(2, 2, 3)
        self.assertEqual(3, l.len())
        node = Node(42)
        l.insert(nodes[0], node)
        self.assertEqual(42, nodes[0].next.value)
