class SimpleTreeNode:
    def __init__(self, val, parent):
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.Children = []  # список дочерних узлов


class SimpleTree:
    def __init__(self, root):
        self.Root = root
        self._len = 1
        # корень, может быть None

    def even_traversal(self, root):
        nodes = []
        if not root:
            nodes.append(self.Root)
            root = self.Root
        for child in root.Children:
            nodes.append(child)
            if len(child.Children):
                nodes.extend(
                    self.even_traversal(child)
                )
        return nodes


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
        return self._len

    def LeafCount(self):
        # количество листьев в дереве
        nodes = self.traversal(self.Root)
        num = 0
        for n in nodes:
            if len(n.Children) == 0:
                num += 1
        return num

    def recursive_even_trees(self, parent=None):
        res = []
        if not parent:
            parent = self.Root
        for child in parent.Children:
            size = len(self.even_traversal(child)) + 1
            if size % 2 == 0:
                res.append(parent)
                res.append(child)
                if size > 2:
                    for grandchild in child.Children:
                        res.extend(
                            self.recursive_even_trees(grandchild)
                        )
            elif size > 2:
                size = len(child.Children)
                for grandchild in child.Children:
                    if size > 0:
                        res.append(child)
                        res.append(grandchild)
                    res.extend(
                        self.recursive_even_trees(grandchild)
                    )
        return res

    def EvenTrees(self):
        return self.recursive_even_trees()
