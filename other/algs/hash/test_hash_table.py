from unittest import TestCase
from other.algs.hash.hash_table import HashTable


class TestLinkedList(TestCase):
    def test_hashfun(self):
        h = HashTable(stp=3, sz=17)
        self.assertEqual(h.hash_fun('a'), 12)

    def test_put_find_value(self):
        h = HashTable(stp=3, sz=17)
        k1 = h.put('a')
        k2 = h.find('a')
        self.assertEqual(k1, k2)

    def test_multiple_eq_hash_values(self):
        h = HashTable(stp=3, sz=17)
        k = h.put("p")
        k1 = h.find("p")
        n = h.put("aa")
        n1 = h.find("aa")
        self.assertEqual(k, k1)
        self.assertEqual(n, n1)
        self.assertNotEqual(k, n)
        self.assertNotEqual(k1, n1)


