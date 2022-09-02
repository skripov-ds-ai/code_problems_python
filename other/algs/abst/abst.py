class aBST:
    def __init__(self, depth):
        # правильно рассчитайте размер массива для дерева глубины depth:
        self.tree_size = 2 ** (depth + 1) - 1
        self.Tree = [None] * self.tree_size
        # массив ключей

    def FindKeyIndex(self, key):
        # ищем в массиве индекс ключа
        idx = 0
        old_idx = 0
        while idx < self.tree_size:
            if self.Tree[idx] is None:
                return -idx
            if self.Tree[idx] == key:
                return idx
            old_idx = 2 * (idx + 1)
            if self.Tree[idx] > key:
                old_idx -= 1
            idx = old_idx

        return None
        # не найден

    def AddKey(self, key):
        result = self.FindKeyIndex(key)
        if result is None:
            return -1
        # добавляем ключ в массив
        result = abs(result)
        self.Tree[result] = key
        return result
        # индекс добавленного/существующего ключа или -1 если не удалось
