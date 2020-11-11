from unittest import TestCase
from other.algs.dynamic_array.dynamic_array import DynArray


class TestLinkedList(TestCase):
    def make_list(self, *vals):
        a = DynArray()
        for v in vals:
            a.append(v)
        return a

    def test_print(self):
        a = self.make_list(1, 2, 3, 4, 5, 1)
        for i in range(a.count):
            print(a[i])
        print(f"count = {a.count}")
        print(f"capacity = {a.capacity}")
        # self.assertListEqual(nodes, found)

    def test_print1(self):
        t = [1] * 10 + [2] * 6
        a = self.make_list(*t)
        for i in range(a.count):
            print(a[i])
        print(f"count = {a.count}")
        print(f"capacity = {a.capacity}")
        # self.assertListEqual(nodes, found)

    def test_print2(self):
        t = [1] * 10 + [2] * 16
        a = self.make_list(*t)
        for i in range(a.count):
            print(a[i])
        print(f"count = {a.count}")
        print(f"capacity = {a.capacity}")
        # self.assertListEqual(nodes, found)

    def test_insert(self):
        t = [2] * 15 + [3]
        a = self.make_list(*t)
        a.insert(0, 1)
        for i in range(a.count):
            print(a[i])
        print(f"count = {a.count}")
        print(f"capacity = {a.capacity}")
        # self.assertListEqual(nodes, found)

    def test_insert1(self):
        t = [2] * 14 + [3]
        a = self.make_list(*t)
        a.insert(0, 1)
        for i in range(a.count):
            print(a[i])
        print(f"count = {a.count}")
        print(f"capacity = {a.capacity}")
        # self.assertListEqual(nodes, found)

    def test_insert2(self):
        t = [2] * 15 + [3]
        a = self.make_list(*t)
        a.insert(16, 1)
        for i in range(a.count):
            print(a[i])
        print(f"count = {a.count}")
        print(f"capacity = {a.capacity}")
        # self.assertListEqual(nodes, found)

    def test_insert3(self):
        t = [2] * 16 + [3]
        a = self.make_list(*t)
        a.insert(15, 1)
        for i in range(a.count):
            print(a[i])
        print(f"count = {a.count}")
        print(f"capacity = {a.capacity}")
        # self.assertListEqual(nodes, found)

    def test_insert4(self):
        t = [2] * 14 + [3]
        a = self.make_list(*t)
        a.insert(15, 1)
        for i in range(a.count):
            print(a[i])
        print(f"count = {a.count}")
        print(f"capacity = {a.capacity}")
        # self.assertListEqual(nodes, found)

    def test_insert5(self):
        t = [2] * 14 + [3]
        a = self.make_list(*t)
        a.insert(12, 1)
        for i in range(a.count):
            print(a[i])
        print(f"count = {a.count}")
        print(f"capacity = {a.capacity}")
        # self.assertListEqual(nodes, found)

    def test_insert6(self):
        t = [2] * 14
        a = self.make_list(*t)
        a.insert(17, 1)
        for i in range(a.count):
            print(a[i])
        print(f"count = {a.count}")
        print(f"capacity = {a.capacity}")
        # self.assertListEqual(nodes, found)

    def test_insert6(self):
        t = [2] * 16 + [3]
        a = self.make_list(*t)
        for i in range(a.count):
            print(a[i])
        print("$$$")
        a.insert(8, 1)
        for i in range(a.count):
            print(a[i])
        print(f"count = {a.count}")
        print(f"capacity = {a.capacity}")
        # self.assertListEqual(nodes, found)

    def test_delete(self):
        t = [1] * 2 + [2] * 16
        a = self.make_list(*t)
        a.delete(0)
        for i in range(a.count):
            print(a[i])
        print(f"count = {a.count}")
        print(f"capacity = {a.capacity}")
        # self.assertListEqual(nodes, found)

    def test_delete1(self):
        t = [1] * 2 + [2] * 16
        a = self.make_list(*t)
        for x in range(3):
            a.delete(0)

        for i in range(a.count):
            print(a[i])
        print(f"count = {a.count}")
        print(f"capacity = {a.capacity}")
        # self.assertListEqual(nodes, found)

    def test_delete2(self):
        t = [2] * 16
        a = self.make_list(*t)
        a.delete(17)

        for i in range(a.count):
            print(a[i])
        print(f"count = {a.count}")
        print(f"capacity = {a.capacity}")
        # self.assertListEqual(nodes, found)
