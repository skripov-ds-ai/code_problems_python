class Heap:
    def __init__(self):
        self.HeapArray = []  # хранит неотрицательные числа-ключи

    def get_left_child_idx(self, idx):
        return 2 * idx + 1

    def get_parent_idx(self, idx):
        return (idx - 1) // 2

    def get_first_empty_idx(self):
        for i, x in enumerate(self.HeapArray):
            if x is None:
                return i
        return -1

    def get_last_idx(self):
        idx = self.get_first_empty_idx()
        if idx == 0:
            return -1
        if idx > 0:
            return idx - 1
        return len(self.HeapArray) - 1

    def check_index_limits(self, idx):
        return -1 < idx < len(self.HeapArray)

    def exists_by_idx(self, idx):
        return self.check_index_limits(idx) and self.HeapArray[idx] is not None

    def swap_heap_elements_by_idxs(self, idx1, idx2):
        self.HeapArray[idx1], self.HeapArray[idx2] = self.HeapArray[idx2], self.HeapArray[idx1]

    def sift_down(self, idx):
        left_idx = self.get_left_child_idx(idx)
        right_idx = left_idx + 1
        goal_idx = left_idx

        left_existance = self.exists_by_idx(left_idx)
        right_existance = self.exists_by_idx(right_idx)
        if not (left_existance or right_existance):
            return

        ok = (not left_existance) or \
             (left_existance and right_existance and self.HeapArray[left_idx] < self.HeapArray[right_idx])
        if ok:
            goal_idx = right_idx

        if self.HeapArray[goal_idx] > self.HeapArray[idx]:
            self.swap_heap_elements_by_idxs(goal_idx, idx)
            self.sift_down(goal_idx)

    def sift_up(self, idx):
        parent_idx = self.get_parent_idx(idx)
        if not self.exists_by_idx(parent_idx):
            return

        if self.HeapArray[parent_idx] < self.HeapArray[idx]:
            self.swap_heap_elements_by_idxs(parent_idx, idx)
            self.sift_up(parent_idx)

    def MakeHeap(self, a, depth):
        # создаём массив кучи HeapArray из заданного
        # размер массива выбираем на основе глубины depth
        self.HeapArray = [None] * (2 ** (depth - 1) + 1)
        for x in a:
            self.Add(x)

    def GetMax(self):
        # вернуть значение корня и перестроить кучу
        if len(self.HeapArray) == 0 or self.HeapArray[0] is None:
            return -1
        # если куча пуста

        root = self.HeapArray[0]
        idx = self.get_last_idx()

        self.HeapArray[0] = self.HeapArray[idx]
        self.HeapArray[idx] = None

        self.sift_down(0)
        return root

    def Add(self, key):
        # добавляем новый элемент key в кучу и перестраиваем её
        idx = self.get_first_empty_idx()

        if idx == -1:
            return False
        # если куча вся заполнена

        self.HeapArray[idx] = key
        self.sift_up(idx)
        return True
