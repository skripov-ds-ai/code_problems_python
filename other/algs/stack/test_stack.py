from unittest import TestCase
from other.algs.stack.stack import Stack


class TestStack(TestCase):
    def make_stack(self, *vals):
        a = Stack()
        for v in vals:
            a.push(v)
        return a

    def test_size(self):
        a = self.make_stack(1, 2, 3, 4, 5, 1)
        print(a.size())

    def test_size_after_pop(self):
        a = self.make_stack(1, 2, 3, 4, 5, 1)
        print(a.size())
        print("nodes\n")
        a.stack.print_all_nodes()
        a.pop()
        print("\n")
        print(a.size())
        print("nodes\n")
        a.stack.print_all_nodes()

    def test_size_after_pop_empty(self):
        a = self.make_stack()
        print(a.size())
        print("nodes\n")
        a.stack.print_all_nodes()
        a.pop()
        print("\n")
        print(a.size())
        print("nodes\n")
        a.stack.print_all_nodes()

    def test_size_after_pop_one_size(self):
        a = self.make_stack(42)
        print(a.size())
        print("nodes\n")
        a.stack.print_all_nodes()
        a.pop()
        print("\n")
        print(a.size())
        print("nodes\n")
        a.stack.print_all_nodes()

    def test_peek_empty(self):
        a = self.make_stack()
        print(a.size())
        print("nodes\n")
        t = a.peek()
        print(f"t = {t}")
        print("\n")
        print(a.size())
        print("nodes\n")
        a.stack.print_all_nodes()

    def test_peek(self):
        a = self.make_stack(42)
        print(a.size())
        print("nodes\n")
        t = a.peek()
        print(f"t = {t}")
        print("\n")
        print(a.size())
        print("nodes\n")
        a.stack.print_all_nodes()

    def test_push(self):
        a = self.make_stack(42)
        print(a.size())
        print("nodes\n")
        a.stack.print_all_nodes()
        a.push(138)
        print("nodes after\n")
        a.stack.print_all_nodes()
        print(f"size = {a.size()}")
