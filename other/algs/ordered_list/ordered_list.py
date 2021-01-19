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


class OrderedList:
    def __init__(self, asc):
        self.clean(asc)

    def __add_in_tail(self, item):
        self.tail.prev.next = item
        item.prev = self.tail.prev
        item.next = self.tail
        self.tail.prev = item
        self._length += 1

    def add_in_tail(self, item):
        item = Node(item)
        self.tail.prev.next = item
        item.prev = self.tail.prev
        item.next = self.tail
        self.tail.prev = item
        self._length += 1

    def __add_in_head(self, newNode):
        self.head.next.prev = newNode
        newNode.next = self.head.next
        newNode.prev = self.head
        self.head.next = newNode
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

        cmp2 = self.compare(node.value, self.tail.prev.value)
        if cmp2 == 1 and self.__ascending or cmp2 == -1 and not self.__ascending:
            self.__add_in_tail(node)
            return
        cmp1 = self.compare(node.value, self.head.next.value)
        if cmp1 == -1 and self.__ascending or cmp1 == 1 and not self.__ascending:
            self.__add_in_head(node)
            return


        self._length += 1
        tmpNode = self.head.next
        while bool(tmpNode):
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
        cmp1 = self.compare(node.value, self.head.next.value)
        if cmp1 == -1 and self.__ascending or cmp1 == 1 and not self.__ascending:
            return None

        cmp2 = self.compare(node.value, self.tail.prev.value)
        if cmp2 == 1 and self.__ascending or cmp2 == -1 and not self.__ascending:
            return None

        tmpNode = self.head.next
        while bool(tmpNode):
            cmp = self.compare(node.value, tmpNode.value)
            if cmp == -1 and self.__ascending or cmp == 1 and not self.__ascending:
                return None
            if cmp == 0:
                return tmpNode
            tmpNode = tmpNode.next
        return None
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

    def clean(self, asc):
        self.head = DummyNode()
        self.tail = DummyNode()
        self.head.next = self.tail
        self.tail.prev = self.head
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
        node = self.head.next
        while bool(node):
            print(node.value)
            node = node.next

    def print_all_reverse_nodes(self):
        node = self.tail.prev
        while bool(node):
            print(node.value)
            node = node.prev


class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        # переопределённая версия для строк
        return super().compare(v1.strip(), v2.strip())
