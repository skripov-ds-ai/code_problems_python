def form_balanced_bst_array(a, idx):
    result_idxs = []
    if a:
        median = len(a) // 2
        result_idxs.append((idx, a[median]))
        new_idx = 2 * idx + 1
        left = form_balanced_bst_array(a[:median], new_idx)
        result_idxs.extend(left)
        right = form_balanced_bst_array(a[median + 1:], new_idx + 1)
        result_idxs.extend(right)
    return result_idxs


def GenerateBBSTArray(a):
    a = sorted(a)
    result = [None] * len(a)
    idxs_tuple = form_balanced_bst_array(a, 0)
    for i, j in idxs_tuple:
        result[i] = j
    return result


class BSTNode:
    def __init__(self, key, parent):
        self.NodeKey = key  # ключ узла
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок
        self.Level = 0  # уровень узла


class BSTFind:  # промежуточный результат поиска
    def __init__(self):
        self.Node = None  # None если
        # в дереве вообще нету узлов

        self.NodeHasKey = False  # True если узел найден
        self.ToLeft = False  # True, если родительскому узлу надо
        # добавить новый узел левым потомком


class BalancedBST:
    def __init__(self):
        self.Root = None  # корень дерева

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

    def make_balance(self, parent, arr, min_idx, max_idx, level):
        if max_idx - min_idx <= 0:
            return None

        median = (max_idx - min_idx) // 2
        key = arr[median]
        node = BSTNode(key, parent)
        node.Level = level

        new_level = level + 1
        node.LeftChild = self.make_balance(
            node,
            arr,
            min_idx,
            median,
            new_level
        )
        node.RightChild = self.make_balance(
            node,
            arr,
            median + 1,
            max_idx,
            new_level
        )

        return node

    def GenerateTree(self, a):
        # создаём дерево с нуля из неотсортированного массива a
        # ...
        arr = sorted(a)
        arr = GenerateBBSTArray(arr)
        new = [arr[0]] + [None] * len(arr)
        current = BSTNode(arr[0], None)
        self.Root = current
        size = len(arr)
        for i in range(1, len(arr)):
            idx = 0
            while True:
                size = len(new)
                idx1 = 2 * idx + 1
                idx2 = idx1 + 1
                if idx1 > size or idx2 > size:
                    return

                if new[idx] > arr[i] and new[idx1] is not None:
                    idx = idx1
                idx1 = 2 * idx + 1
                idx2 = idx1 + 1

                if idx2 > size - 1:
                    new.extend([None] * (idx2 - size))
                size = len(new)

                if new[idx] > arr[i] and new[idx1] is None:
                    idx = idx1
                    new[idx] = arr[i]
                    current = self.FindNodeByKey(new[(idx - 1) // 2])
                    current = current.Node
                    other = BSTNode(new[idx], current)
                    other.Level = current.Level + 1
                    current.LeftChild = other
                    break

                idx1 = 2 * idx + 1
                idx2 = idx1 + 1
                if new[idx] <= arr[i] and new[idx2] is not None:
                    idx = idx2
                idx1 = 2 * idx + 1
                idx2 = idx1 + 1

                if idx2 > size - 1:
                    new.extend([None] * (idx2 - size + 1))
                size = len(new)
                idx1 = 2 * idx + 1
                idx2 = idx1 + 1

                if new[idx] <= arr[i] and new[idx2] is None:
                    idx = idx2
                    new[idx] = arr[i]
                    current = self.FindNodeByKey(new[(idx - 1) // 2])
                    current = current.Node
                    other = BSTNode(new[idx], current)
                    other.Level = current.Level + 1
                    current.RightChild = other
                    break

    def is_balanced_subtree(self, parent):
        if not parent:
            return True, 0
        l, l_height = self.is_balanced_subtree(parent.LeftChild)
        r, r_height = self.is_balanced_subtree(parent.RightChild)
        d = abs(l_height - r_height) < 2
        ok = l and r and d
        return ok, max(l_height, r_height) + 1

    def IsBalanced(self, root_node):
        return self.is_balanced_subtree(root_node)
        # сбалансировано ли дерево с корнем root_node