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
        l.print_all_reverse_nodes()
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
        l.print_all_reverse_nodes()
        print("\n$\n")
        l.print_all_nodes()
        node = l.find(0)
        self.assertIsNotNone(node)
        self.assertEqual(node.value, 0)
        self.assertEqual(node.prev.value, 1)
        with self.assertRaises(AttributeError):
            node.next.value
        # TODO: there are a series of problems!!

    def test_empty(self):
        l = OrderedList(asc=True)
        self.assertEqual(l.len(), 0)


