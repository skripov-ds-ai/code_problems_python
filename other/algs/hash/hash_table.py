class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        # в качестве value поступают строки!
        h = 0
        # m = 1e9 + 7
        p = 31
        for v in value:
            h = (h * p + ord(v)) % self.size
        # всегда возвращает корректный индекс слота
        return h

    def seek_slot(self, value):
        # находит индекс пустого слота для значения, или None
        k = self.hash_fun(value)
        if self.slots[k] is None:
            return k
        for i in range(self.size):
            k = (k + self.step) % self.size
            if self.slots[k] is None:
                return k
        return None

    def put(self, value):
        # записываем значение по хэш-функции
        k = self.seek_slot(value)
        if isinstance(k, int):
            self.slots[k] = value
            return k
        # возвращается индекс слота или None,
        # если из-за коллизий элемент не удаётся
        # разместить
        return None

    def find(self, value):
        # k = self.seek_slot(value)
        # if isinstance(k, int) and self.slots[k] is not None:
        #     return k
        k = self.hash_fun(value)
        if self.slots[k] == value:
            return k
        for i in range(self.size):
            k = (k + self.step) % self.size
            if self.slots[k] == value:
                return k
        # находит индекс слота со значением, или None
        return None
