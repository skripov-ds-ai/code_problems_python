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
        curr = self.Root
        while curr:
            if curr.NodeKey == key:
                t.Node = curr
                t.NodeHasKey = True
                curr = None
            elif curr.NodeKey < key:
                if curr.RightChild:
                    curr = curr.RightChild
                else:
                    t.Node = curr
                    curr = None
            else:
                if curr.LeftChild:
                    curr = curr.LeftChild
                else:
                    t.Node = curr
                    t.ToLeft = True
                    curr = None
        return t
        # ищем в дереве узел и сопутствующую информацию по ключу
        # возвращает BSTFind

    def AddKeyValue(self, key, val):
        t = self.FindNodeByKey(key)
        new = BSTNode(key, val, None)
        if t.Node is None:
            self.Root = new
            self._len += 1
            return True
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
        if t.Node and t.NodeHasKey:
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

    def DeepAllNodes(self, mode):
        return self.deep(self.Root, mode)

    def deep(self, root, mode):
        if not root:
            return []
        nodes = []
        left = self.deep(root.LeftChild, mode)
        right = self.deep(root.RightChild, mode)
        if mode == 0:
            nodes.extend(left)
            nodes.append(root)
            nodes.extend(right)
        elif mode == 1:
            nodes.extend(left)
            nodes.extend(right)
            nodes.append(root)
        else:
            nodes.append(root)
            nodes.extend(left)
            nodes.extend(right)
        return nodes

    def WideAllNodes(self):
        return self.wide(self.Root)

    def wide(self, root):
        if not root:
            return []
        q = [root]
        nodes = [root]
        while q:
            node = q.pop()
            if node.LeftChild:
                nodes.append(node.LeftChild)
                q.append(node.LeftChild)
            if node.RightChild:
                nodes.append(node.RightChild)
                q.append(node.RightChild)
        return nodes
    #     if not root:
    #         return []
    #     nodes = [root]
    #     if root.LeftChild:
    #         nodes.extend(self.wide(root.LeftChild))
    #     if root.RightChild:
    #         nodes.extend(self.wide(root.LeftChild))
    #     return nodes
