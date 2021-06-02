class SimpleTreeNode:
    def __init__(self, val, parent):
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.Children = []  # список дочерних узлов

    def __str__(self):
        return str(self.NodeValue)


class SimpleTree:
    def __init__(self, root):
        self.Root = root
        self._len = 1
        # корень, может быть None

    def traversal(self, root, p=False):
        nodes = []
        if root:
            if p:
                print("traversal", root.NodeValue)
            for child in root.Children:
                tmp = self.traversal(child)
                if p:
                    print("traversal", [x.NodeValue for x in tmp])
                nodes.extend(tmp)
            nodes.append(root)
        return nodes

    def AddChild(self, ParentNode, NewChild):
        ParentNode.Children.append(NewChild)
        NewChild.Parent = ParentNode
        self._len += 1
        # pass  # ваш код добавления нового дочернего узла существующему ParentNode

    def DeleteNode(self, NodeToDelete):
        nodes = self.traversal(self.Root)
        to_del = None
        for node in nodes:
            if NodeToDelete is node and NodeToDelete is not self.Root:
                to_del = node
                t = to_del.Parent.Children
                to_del.Parent.Children.remove(to_del)
                # to_del.Parent.Children.extend(to_del.Children)
                self._len -= 1
                break
        # ваш код удаления существующего узла NodeToDelete

    def GetAllNodes(self):
        # ваш код выдачи всех узлов дерева в определённом порядке
        return self.traversal(self.Root)

    def FindNodesByValue(self, val):
        # ваш код поиска узлов по значению
        nodes = self.traversal(self.Root)
        new_nodes = []
        for node in nodes:
            if node.NodeValue == val:
                new_nodes.append(node)
        return new_nodes

    def MoveNode(self, OriginalNode, NewParent):
        # ваш код перемещения узла вместе с его поддеревом --
        # в качестве дочернего для узла NewParent
        NewParent.Children.append(OriginalNode)
        t = OriginalNode.Parent.Children
        t.remove(OriginalNode)
        OriginalNode.Parent = NewParent

    def Count(self):
        # количество всех узлов в дереве
        # return self._len
        return self.RecursiveCount(self.Root)

    def LeafCount(self):
        # количество листьев в дереве
        nodes = self.traversal(self.Root)
        num = 0
        for n in nodes:
            if len(n.Children) == 0:
                num += 1
        return num

    def RecursiveCount(self, root):
        if root is None:
            return 0
        tmp = 1
        for child in root.Children:
            tmp += self.RecursiveCount(child)
        return tmp

    def EvenTrees(self):
        size = self.Count()
        if size % 2 == 1 or size == 0:
            return []

        nodes = []
        for child in self.Root.Children:
            t = SimpleTree(child)
            if t.Count() % 2 == 0:
                nodes.append(self.Root)
                nodes.append(child)
            nodes.extend(t.EvenTrees())
        return nodes
