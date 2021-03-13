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

    def FindNodeByKey(self, key):
        t = BSTFind()
        t.Node = self.Root
        if t.Node.NodeKey == key:
            t.NodeHasKey = True
            return t
        while t.Node.NodeKey != key:
            if key >= t.Node.NodeKey:
                if not t.Node.RightChild:
                    break
                t.Node = t.Node.RightChild
            else:
                if not t.Node.LeftChild:
                    t.ToLeft = True
                    break
                t.Node = t.Node.LeftChild
        t.NodeHasKey = t.Node.NodeKey == key
        return t
        # ищем в дереве узел и сопутствующую информацию по ключу
        # возвращает BSTFind

    def AddKeyValue(self, key, val):
        t = self.FindNodeByKey(key)
        new = BSTNode(key, val, None)
        if not t.NodeHasKey:
            self._len += 1
            new.Parent = t.Node
            if t.ToLeft:
                t.Node.LeftChild = new
            else:
                t.Node.RightChild = new
            return True
        return False
        # добавляем ключ-значение в дерево
        # если ключ уже есть

    def FinMinMax(self, FromNode, FindMax):
        node = FromNode
        if FindMax:
            while node.RightChild:
                node = node.RightChild
        else:
            while node.LeftChild:
                node = node.LeftChild
        return node
        # ищем максимальный/минимальный ключ в поддереве
        # возвращается объект типа BSTNode

    def DeleteNodeByKey(self, key, real=True):
        t = self.FindNodeByKey(key)
        if t.NodeHasKey:
            if real:
                self._len -= 1
            node = t.Node
            tmp = None
            if node.LeftChild and node.RightChild is None:
                tmp = node.LeftChild
            elif node.LeftChild is None and node.RightChild:
                tmp = node.RightChild
            elif node.LeftChild and node.RightChild:
                successor = self.FinMinMax(node.RightChild, False)
                self.DeleteNodeByKey(successor.NodeKey, False)
                successor.LeftChild = node.LeftChild
                successor.RightChild = node.RightChild
                tmp = successor
            if node is self.Root:
                self.Root = tmp
                if tmp:
                    self.Root.Parent = None
            else:
                if node.Parent.LeftChild is node:
                    node.Parent.LeftChild = tmp
                else:
                    node.Parent.RightChild = tmp
                if tmp:
                    tmp.Parent = node.Parent
            return True
        return False
        # удаляем узел по ключу
        # если узел не найден

    def Count(self):
        return self._len
        # количество узлов в дереве
