from unittest import TestCase
from other.algs.associative_array.native_array import NativeDictionary


class TestLinkedList(TestCase):
    def test_hashfun(self):
        h = NativeDictionary(sz=17)
        self.assertEqual(h.hash_fun('a'), 12)

    def test_put_find_value(self):
        h = NativeDictionary(sz=17)
        h.put('a', 3)
        v = h.get('a')
        self.assertEqual(v, 3)

    def test_multiple_eq_hash_values(self):
        h = NativeDictionary(sz=17)
        h.put("p", 1)
        k1 = h.get("p")
        h.put("aa", 3)
        n1 = h.get("aa")
        self.assertEqual(k1, 1)
        self.assertEqual(n1, 3)

    def test_is_key(self):
        h = NativeDictionary(sz=17)
        h.put("p", 1)
        h.put("c", 3)
        h.put("aa", 42)
        self.assertTrue(h.is_key("p"))
        self.assertTrue(h.is_key("c"))
        self.assertTrue(h.is_key("aa"))


