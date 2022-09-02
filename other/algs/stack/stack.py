class DummyNode:
    def __init__(self):
        self.prev = None
        self.next = None

    def __bool__(self):
        return False


class Node(DummyNode):
    def __init__(self, v):
        super().__init__()
        self.value = v

    def __bool__(self):
        return True


class LinkedList2:
    def __init__(self):
        self.clean()

    def add_in_tail(self, item):
        self.tail.prev.next = item
        item.prev = self.tail.prev
        item.next = self.tail
        self.tail.prev = item
        self._length += 1

    def find(self, val):
        if self._length == 0:
            return None

        node = self.head.next
        while bool(node):
            if node.value == val:
                return node
            node = node.next
        return None
        # здесь будет ваш код

    def find_all(self, val):
        if self._length == 0:
            return None

        elems = []
        node = self.head.next
        while bool(node):
            if node.value == val:
                elems.append(node)
            node = node.next
        return elems
        # здесь будет ваш код

    def delete(self, val, all=False):
        node = self.head.next
        prev = self.head
        ok = True

        while bool(node):
            if bool(node) and node.value == val:
                while bool(node) and node.value == val:
                    node = node.next
                    self._length -= 1
                    node.prev = prev
                    if not all:
                        ok = False
                        break
                prev.next = node
                node.prev = prev

            if not ok:
                break
            prev = node
            if node:
                node = node.next
        # здесь будет ваш код

    def clean(self):
        self.head = DummyNode()
        self.tail = DummyNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self._length = 0
        # здесь будет ваш код

    def len(self):
        return self._length
        # здесь будет ваш код

    def insert(self, afterNode, newNode):
        if newNode is None or not bool(newNode):
            return

        if self._length == 0 or afterNode is None and self._length > 0:
            self.add_in_tail(newNode)
            return

        self._length += 1
        if afterNode.next:
            afterNode.next.prev = newNode
        newNode.next = afterNode.next
        afterNode.next = newNode
        newNode.prev = afterNode

    def add_in_head(self, newNode):
        self.head.next.prev = newNode
        newNode.next = self.head.next
        newNode.prev = self.head
        self._length += 1
        # здесь будет ваш код

    def print_all_nodes(self):
        node = self.head.next
        while bool(node):
            print(node.value)
            node = node.next

    def print_all_reverse_nodes(self):
        node = self.tail.prev
        while bool(node):
            print(node.value)
            node = node.prev


class Stack:
    def __init__(self):
        self.stack = LinkedList2()

    def size(self):
        return self.stack.len()

    def pop(self, delete=True):
        # ваш код
        if self.stack.len():
            tmp = self.stack.tail.prev
            if delete and bool(tmp):
                self.stack.tail.prev = self.stack.tail.prev.prev
                self.stack.tail.prev.next = self.stack.tail
                self.stack._length -= 1
            if bool(tmp):
                return tmp.value
        return None
        # если стек пустой

    def push(self, value):
        self.stack.add_in_tail(Node(value))

    def peek(self):
        return self.pop(delete=False)
        # если стек пустой

