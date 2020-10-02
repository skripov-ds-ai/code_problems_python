class Node:
    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        # accumulator
        self._length = 0

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item
        self._length += 1

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        elems = []
        node = self.head
        while node:
            if node.value == val:
                elems.append(node)
            node = node.next
        return elems
        # здесь будет ваш код

    def delete(self, val, all=False):
        node = self.head
        prev = None

        if node and node.value == val:
            while node and node.value == val:
                self._length -= 1
                node = node.next
                if not all:
                    return
            prev = node
            self.head = node

        while node:
            if node.value == val:
                while node and node.value == val:
                    node = node.next
                    self._length -= 1
                    if not all:
                        return
                prev.next = node
            prev = node
            if node:
                node = node.next
        # здесь будет ваш код

    def clean(self):
        self.head = None
        self.tail = None
        self._length = 0
        # здесь будет ваш код

    def len(self):
        return self._length
        # здесь будет ваш код

    def insert(self, afterNode, newNode):
        if not self.head and not self.tail and not afterNode:
            self.add_in_tail(newNode)
            return

        self._length += 1

        if not afterNode:
            newNode.next = self.head
            self.head = newNode
            return

        node = self.head
        while node is not afterNode:
            node = node.next
        if node.next and node.next.next:
            newNode.next = node.next.next
        node.next = newNode
        # здесь будет ваш код

