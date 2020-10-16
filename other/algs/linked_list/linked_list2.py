class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None
        # accumulator
        self._length = 0

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item
        self._length += 1

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None
        # здесь будет ваш код

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

        ok = True

        if node and node.value == val:
            while node and node.value == val:
                self._length -= 1
                node = node.next
                if node:
                    node.prev = prev
                if not all:
                    ok = False
                    self.head = node
                    break
            prev = node
            self.head = node

        if ok:
            while node:
                if node.value == val:
                    while node and node.value == val:
                        node = node.next
                        self._length -= 1
                        if node:
                            node.prev = prev
                        if not all:
                            ok = False
                            break
                    prev.next = node
                    if node:
                        node.prev = prev

                if not ok:
                    break
                prev = node
                if node:
                    node = node.next

        node = self.head
        while node:
            if not node.next:
                self.tail = node
            node = node.next
        if self._length == 0:
            self.tail = None
        if not self.head:
            self.tail = None
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
        if not newNode:
            return

        if self._length == 0 or not afterNode and self._length > 0:
            self.add_in_tail(newNode)
            return

        self._length += 1
        newNode.next = afterNode.next
        afterNode.next = newNode
        if newNode and not newNode.next:
            self.tail = newNode

    def add_in_head(self, newNode):
        if self.tail is None:
            self.tail = newNode
            newNode.prev = None
            newNode.next = None
        else:
            self.head.prev = newNode
            newNode.next = self.tail
        self.head = newNode
        self._length += 1
        # здесь будет ваш код

    # TODO: remove
    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    # TODO: remove
    def print_all_reverse_nodes(self):
        node = self.tail
        while node != None:
            print(node.value)
            node = node.prev