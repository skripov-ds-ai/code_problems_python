class Deque:
    def __init__(self):
        self.q = []
        # инициализация внутреннего хранилища

    def addFront(self, item):
        # добавление в голову
        self.q.insert(0, item)

    def addTail(self, item):
        # добавление в хвост
        self.q.append(item)

    def removeFront(self):
        # удаление из головы
        if self.size():
            t = self.q.pop(0)
            return t
        return None
        # если очередь пуста

    def removeTail(self):
        # удаление из хвоста
        if self.size():
            t = self.q.pop()
            return t
        return None
        # если очередь пуста

    def size(self):
        return len(self.q)
        # размер очереди