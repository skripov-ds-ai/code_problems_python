class BSTNode:
    def __init__(self, key, val, parent):
        self.NodeKey = key  # ключ узла
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок


class BSTFind:  # промежуточный результат поиска
    def __init__(self):
        self.Node = None  # None если
        # в дереве вообще нету узлов

        self.NodeHasKey = False  # True если узел найден
        self.ToLeft = False  # True, если родительскому узлу надо
        # добавить новый узел левым потомком


class BST:
    def __init__(self, node):
        self.Root = node  # корень дерева, или None
        self._len = 1

    def find(self, root, key, left):
        # if root is None:
        #     t = BSTFind()
        #     t.Node = root
        #     t.ToLeft = left
        #     return t
        if root.NodeKey == key:
            t = BSTFind()
            t.Node = root
            t.NodeHasKey = True
            t.ToLeft = left
            return t
        if root.NodeKey > key:
            if root.LeftChild is None:
                t = BSTFind()
                t.Node = root
                t.ToLeft = True
                return t
            return self.find(root.LeftChild, key, True)
        if root.RightChild is None:
            t = BSTFind()
            t.Node = root
            t.ToLeft = False
            return t
        return self.find(root.RightChild, key, False)

    def FindNodeByKey(self, key):
        # ищем в дереве узел и сопутствующую информацию по ключу
        return self.find(self.Root, key, False)
        # возвращает BSTFind

    def AddKeyValue(self, key, val):
        # добавляем ключ-значение в дерево
        t = self.find(self.Root, key, False)
        if t.NodeHasKey:
            return False
        node = BSTNode(key, val, t.Node)
        node.Parent = t
        if t.ToLeft:
            t.Node.LeftChild = node
        else:
            t.Node.RightChild = node
        self._len += 1
        return True
        # если ключ уже есть

    def find_min_max(self, root, mx=True):
        if mx:
            if root.RightChild:
                return self.find_min_max(root.RightChild, mx=mx)
            t = BSTFind()
            t.Node = root
            t.NodeHasKey = True
            return t
        if root.LeftChild:
            return self.find_min_max(root.LeftChild, mx=mx)
        t = BSTFind()
        t.Node = root
        t.NodeHasKey = True
        return t

    def FinMinMax(self, FromNode, FindMax):
        # ищем максимальный/минимальный ключ в поддереве
        # возвращается объект типа BSTNode
        return self.find_min_max(FromNode, FindMax)

    def find_successor(self, root):
        if root.RightChild:
            node = root.RightChild
            while node.LeftChild:
                node = node.LeftChild
            return node, True
        return root.LeftChild, False

    def delete_node(self, root, key):
        parent = None
        curr = root

        while curr and curr.NodeKey != key:
            parent = curr
            if key < curr.NodeKey:
                curr = curr.LeftChild
            else:
                curr = curr.RightChild

        if curr is None:
            return root

        if curr.LeftChild is None and curr.RightChild is None:
            if curr != root:
                if parent.LeftChild == curr:
                    parent.LeftChild = None
                else:
                    parent.RightChild = None
            else:
                root = None
        elif curr.LeftChild and curr.RightChild:
            successor = self.FinMinMax(curr.RightChild, False)
            key = successor.Node.NodeKey
            value = successor.Node.NodeValue
            self.delete_node(successor.Node, key)
            curr.NodeKey = key
            curr.NodeValue = value
        else:
            if curr.LeftChild:
                child = curr.LeftChild
            else:
                child = curr.RightChild
            if curr != root:
                if curr == parent.LeftChild:
                    parent.LeftChild = child
                else:
                    parent.RightChild = child
                child.Parent = parent
            else:
                root = child
                child.Parent = None
        return root

    def DeleteNodeByKey(self, key):
        # удаляем узел по ключу
        t = self.find(self.Root, key, False)
        if not t.NodeHasKey:
            return False
        self._len -= 1
        self.delete_node(self.Root, key)
        return True  # если узел не найден

    def Count(self):
        return self._len
        # количество узлов в дереве
