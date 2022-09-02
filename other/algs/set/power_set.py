class HashTable:
    def __init__(self, sz):
        self.sz = sz
        self.slots = [[]] * self.sz
        self._length = 0

    def hash_fun(self, value):
        # в качестве value поступают строки!
        h = 0
        # m = 1e9 + 7
        p = 31
        for v in value:
            h = (h * p + ord(v)) % self.sz
        # всегда возвращает корректный индекс слота
        return h

    def seek_slot(self, value):
        # находит индекс пустого слота для значения, или None
        k = self.hash_fun(value)
        return k

    def put(self, value):
        # записываем значение по хэш-функции
        k = self.seek_slot(value)
        for x in self.slots[k]:
            if x == value:
                return
        self.slots[k].append(value)
        self._length += 1
        # возвращается индекс слота или None,
        # если из-за коллизий элемент не удаётся
        # разместить
        # return None

    def find(self, value):
        k = self.hash_fun(value)
        for x in self.slots[k]:
            if x == value:
                return k
        # находит индекс слота со значением, или None
        return None


# наследуйте этот класс от HashTable
# или расширьте его методами из HashTable
class PowerSet(HashTable):
    def __init__(self):
        # ваша реализация хранилища
        super().__init__(200)

    def size(self):
        return self._length
        # количество элементов в множестве

    def get(self, value):
        # возвращает True если value имеется в множестве,
        # иначе False
        return self.find(value) is not None

    def remove(self, value):
        # возвращает True если value удалено
        # иначе False
        k = self.find(value)
        if k is None:
            return False
        for i in range(len(self.slots[k])):
            if self.slots[k][i] == value:
                self.slots[k].pop(i)
                self._length -= 1
                return True
        return False

    def intersection(self, set2):
        p = PowerSet()
        for slot in self.slots:
            for elem in slot:
                if set2.get(elem):
                    p.put(elem)
        # пересечение текущего множества и set2
        return p

    def union(self, set2):
        p = PowerSet()
        for slot in self.slots:
            for elem in slot:
                p.put(elem)
        for slot in set2.slots:
            for elem in slot:
                p.put(elem)
        # объединение текущего множества и set2
        return p

    def difference(self, set2):
        inter = self.intersection(set2)
        p = PowerSet()
        for slot in self.slots:
            for elem in slot:
                if not inter.get(elem):
                    p.put(elem)
        # разница текущего множества и set2
        return p

    def issubset(self, set2):
        if set2.size() == 0:
            return True
        for slot in set2.slots:
            for elem in slot:
                if not self.get(elem):
                    return False
        # возвращает True, если set2 есть
        # подмножество текущего множества,
        # иначе False
        return True