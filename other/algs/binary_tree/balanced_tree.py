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


class BalancedBST:
    def __init__(self):
        self.Root = None  # корень дерева

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
        self.Root = self.make_balance(None, arr, 0, len(a), 1)

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