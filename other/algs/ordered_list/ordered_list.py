class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class OrderedList:
    def __init__(self, asc):
        self.clean(asc)

    def __add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item
        self._length += 1

    def add_in_tail(self, item):
        item = Node(item)
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item
        self._length += 1

    def __add_in_head(self, newNode):
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

    def compare(self, v1, v2):
        if v1 < v2:
            return -1
        if v1 > v2:
            return 1
        return 0
        # -1 если v1 < v2
        # 0 если v1 == v2
        # +1 если v1 > v2

    def add(self, value):
        node = Node(value)

        if self._length == 0:
            self.__add_in_tail(node)
            return

        cmp2 = self.compare(node.value, self.tail.value)
        if cmp2 == 1 and self.__ascending or cmp2 == -1 and not self.__ascending:
            self.__add_in_tail(node)
            return
        cmp1 = self.compare(node.value, self.head.value)
        if cmp1 == -1 and self.__ascending or cmp1 == 1 and not self.__ascending:
            self.__add_in_head(node)
            return

        self._length += 1
        tmpNode = self.head
        while tmpNode:
            cmp = self.compare(node.value, tmpNode.value)
            if cmp == -1 and self.__ascending or cmp == 1 and not self.__ascending:
                node.prev = tmpNode.prev
                node.next = tmpNode
                tmpNode.prev.next = node
                tmpNode.prev = node
                break
            tmpNode = tmpNode.next

        # автоматическая вставка value
        # в нужную позицию

    def find(self, val):
        node = Node(val)
        cmp1 = self.compare(node.value, self.head.value)
        if cmp1 == -1 and self.__ascending or cmp1 == 1 and not self.__ascending:
            return None

        cmp2 = self.compare(node.value, self.tail.value)
        if cmp2 == 1 and self.__ascending or cmp2 == -1 and not self.__ascending:
            return None

        tmpNode = self.head
        while tmpNode:
            cmp = self.compare(node.value, tmpNode.value)
            if cmp == -1 and self.__ascending or cmp == 1 and not self.__ascending:
                return None
            if cmp == 0:
                return tmpNode
            tmpNode = tmpNode.next
        return None
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

    def clean(self, asc):
        self.head = None
        self.tail = None
        self._length = 0
        self.__ascending = asc

    def len(self):
        return self._length
        # здесь будет ваш код

    def get_all(self):
        r = []
        node = self.head
        while node:
            r.append(node)
            node = node.next
        return r

    def print_all_nodes(self):
        node = self.head
        while node:
            print(node.value)
            node = node.next

    def print_all_reverse_nodes(self):
        node = self.tail
        while node:
            print(node.value)
            node = node.prev


class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        # переопределённая версия для строк
        return super(OrderedStringList, self).compare(v1.strip(), v2.strip())
