class NativeDictionary:
    def __init__(self, sz):
        self.step = 3
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
        # в качестве key поступают строки!
        # всегда возвращает корректный индекс слота
        h = 0
        # m = 1e9 + 7
        p = 31
        for v in key:
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

    def iterate_keys(self, value):
        k = self.hash_fun(value)
        if self.slots[k] == value:
            return k
        for i in range(self.size):
            k = (k + self.step) % self.size
            if self.slots[k] == value:
                return k
        return None

    def is_key(self, key):
        k = self.hash_fun(key)
        if self.slots[k] == key:
            return True
        for i in range(self.size):
            k = (k + self.step) % self.size
            if self.slots[k] == key:
                return True
        # возвращает True если ключ имеется,
        # иначе False
        return False

    def put(self, key, value):
        k = self.seek_slot(key)
        if isinstance(k, int):
            self.slots[k] = key
            self.values[k] = value
        # гарантированно записываем
        # значение value по ключу key

    def get(self, key):
        k = self.iterate_keys(key)
        if isinstance(k, int):
            return self.values[k]
        # возвращает value для key,
        # или None если ключ не найден
        return None