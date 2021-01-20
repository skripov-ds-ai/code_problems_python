from unittest import TestCase
from other.algs.ordered_list.ordered_list import OrderedList


class TestOrderedList(TestCase):
    def make_list(self, asc, *vals):
        l = OrderedList(asc=asc)
        for v in vals:
            l.add(v)
        return l

    def test_add_empty(self):
        l = self.make_list(True)
        self.assertEqual(l.len(), 0)
        l.add(0)
        self.assertEqual(l.len(), 1)

    def test_add_nonempty(self):
        l = self.make_list(True, 1)
        self.assertEqual(l.len(), 1)
        l.add(0)
        self.assertEqual(l.len(), 2)
        l.add(2)
        self.assertEqual(l.len(), 3)

    def test_add_nonempty_asc_False(self):
        l = self.make_list(True)
        l.clean(asc=False)
        self.assertEqual(l.len(), 0)

        l.add(1)
        self.assertEqual(l.len(), 1)

        l.add(0)
        self.assertEqual(l.len(), 2)

        l.add(2)
        self.assertEqual(l.len(), 3)

    def test_find(self):
        l = self.make_list(True, 0, 1, 3, 2)
        node = l.find(2)
        self.assertIsNotNone(node)
        self.assertEqual(node.value, 2)
        self.assertEqual(node.prev.value, 1)
        self.assertEqual(node.next.value, 3)

    def test_find_first(self):
        l = self.make_list(True, 0, 1, 3, 2)
        node = l.find(0)
        self.assertIsNotNone(node)
        self.assertEqual(node.value, 0)
        self.assertEqual(node.next.value, 1)
        with self.assertRaises(AttributeError):
            node.prev.value

    def test_find_last(self):
        l = self.make_list(True, 0, 1, 3, 2)
        node = l.find(3)
        self.assertIsNotNone(node)
        self.assertEqual(node.value, 3)
        self.assertEqual(node.prev.value, 2)
        with self.assertRaises(AttributeError):
            node.next.value

    def test_find_last_desc(self):
        l = self.make_list(False, 0, 1, 3, 2)
        node = l.find(0)
        self.assertIsNotNone(node)
        self.assertEqual(node.value, 0)
        self.assertEqual(node.prev.value, 1)
        with self.assertRaises(AttributeError):
            node.next.value

    def test_empty(self):
        l = OrderedList(asc=True)
        self.assertEqual(l.len(), 0)

    def test_delete(self):
        l = self.make_list(True, 0, 1, 5, 4, 3, 2)
        self.assertEqual(l.len(), 6)
        l.delete(0)
        self.assertEqual(l.len(), 5)
        node = l.find(0)
        self.assertIsNone(node)

    def test_delete(self):
        l = self.make_list(False, 0, 1, 5, 4, 3, 2)
        self.assertEqual(l.len(), 6)
        l.delete(0)
        self.assertEqual(l.len(), 5)
        node = l.find(0)
        self.assertIsNone(node)

    def test_delete_empty(self):
        l = self.make_list(True)
        self.assertEqual(l.len(), 0)
        l.delete(0)
        self.assertEqual(l.len(), 0)

    def test_len_with_delete_head(self):
        l = OrderedList(True)
        l.add(65)
        self.assertEqual(l.head.value, 65)
        self.assertEqual(l.tail.value, 65)
        l.add(42)
        self.assertEqual(l.head.value, 42)
        self.assertEqual(l.tail.value, 65)
        l.add(0)
        self.assertEqual(l.head.value, 0)
        self.assertEqual(l.tail.value, 65)
        self.assertEqual(l.len(), 3)
        l.delete(0)
        self.assertEqual(l.head.value, 42)
        self.assertEqual(l.tail.value, 65)
        self.assertEqual(l.len(), 2)
        l.add(1)
        self.assertEqual(l.head.value, 1)
        self.assertEqual(l.tail.value, 65)
        self.assertEqual(l.len(), 3)
        l.delete(42)
        self.assertEqual(l.head.value, 1)
        self.assertEqual(l.tail.value, 65)
        self.assertEqual(l.len(), 2)
        l.delete(65)
        self.assertEqual(l.head.value, 1)
        self.assertEqual(l.tail.value, 1)
        self.assertEqual(l.len(), 1)

    def test_len_with_delete_tail(self):
        l = OrderedList(True)
        l.add(65)
        self.assertEqual(l.len(), 1)
        l.add(65)
        self.assertEqual(l.len(), 2)
        l.add(0)
        self.assertEqual(l.len(), 3)
        l.delete(65)
        self.assertEqual(l.len(), 2)
        # l.print_all_nodes()
        # l.print_all_reverse_nodes()
        l.delete(65)
        # l.print_all_nodes()
        self.assertEqual(l.len(), 1)

    def test_len_with_add_synonyms_to_head_then_delete(self):
        l = OrderedList(True)
        l.add(65)
        self.assertEqual(l.len(), 1)
        l.add(65)
        self.assertEqual(l.len(), 2)
        l.add(1000)
        self.assertEqual(l.len(), 3)
        l.delete(65)
        self.assertEqual(l.len(), 2)
        l.delete(65)
        self.assertEqual(l.len(), 1)


