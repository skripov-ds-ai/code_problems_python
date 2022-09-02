from unittest import TestCase
from other.algs.set.power_set import PowerSet


class TestPowerSet(TestCase):
    def test_size(self):
        p = PowerSet()
        p.put("1")
        self.assertEqual(p.size(), 1)
        p.put("1")
        self.assertEqual(p.size(), 1)

    def test_size_empty(self):
        p = PowerSet()
        self.assertEqual(p.size(), 0)

    def test_size_after_remove_empty(self):
        p = PowerSet()
        self.assertEqual(p.size(), 0)
        p.put("1")
        self.assertEqual(p.size(), 1)
        p.put("1")
        self.assertEqual(p.size(), 1)
        p.remove("1")
        self.assertEqual(p.size(), 0)

    def test_size_after_additional_remove(self):
        p = PowerSet()
        p.put("1")
        self.assertEqual(p.size(), 1)
        p.put("1")
        self.assertEqual(p.size(), 1)
        p.remove("1")
        self.assertEqual(p.size(), 0)
        p.remove("1")
        self.assertEqual(p.size(), 0)

    def test_issubset_empty(self):
        p = PowerSet()
        t = PowerSet()
        self.assertTrue(p.issubset(t))
        self.assertTrue(p.issubset(p))
        self.assertTrue(t.issubset(p))
        self.assertTrue(t.issubset(t))

    def test_issubset(self):
        p = PowerSet()
        p.put("42")
        p.put("4242")
        t = PowerSet()
        self.assertTrue(p.issubset(t))
        self.assertTrue(p.issubset(p))
        self.assertFalse(t.issubset(p))

    def test_issubset_nonempty(self):
        p = PowerSet()
        p.put("42")
        p.put("4242")
        t = PowerSet()
        t.put("42")
        self.assertTrue(p.issubset(t))
        self.assertTrue(p.issubset(p))
        self.assertFalse(t.issubset(p))

    def test_union_empty(self):
        p = PowerSet()
        t = PowerSet()
        u = p.union(t)
        self.assertEqual(u.size(), 0)

    def test_union(self):
        p = PowerSet()
        p.put("42")
        t = PowerSet()
        t.put("1")
        u = p.union(t)
        self.assertEqual(u.size(), 2)

    def test_union_equal(self):
        p = PowerSet()
        p.put("42")
        t = PowerSet()
        t.put("42")
        u = p.union(t)
        self.assertEqual(u.size(), 1)

    def test_intersection(self):
        p = PowerSet()
        p.put("1")
        p.put("2")
        p.put("3")
        t = PowerSet()
        t.put("1")
        t.put("3")
        u = p.intersection(t)
        self.assertEqual(u.size(), 2)

    def test_intersection_different(self):
        p = PowerSet()
        p.put("1")
        p.put("2")
        p.put("3")
        t = PowerSet()
        t.put("0")
        t.put("4")
        u = p.intersection(t)
        self.assertEqual(u.size(), 0)

    def test_difference_different(self):
        p = PowerSet()
        p.put("1")
        p.put("2")
        p.put("3")
        t = PowerSet()
        t.put("24")
        t.put("42")
        u = p.difference(t)
        self.assertEqual(p.size() - u.size(), 0)

    def test_difference_with_common(self):
        p = PowerSet()
        p.put("1")
        p.put("2")
        p.put("3")
        t = PowerSet()
        t.put("1")
        t.put("2")
        u = p.difference(t)
        self.assertEqual(u.size(), 1)


