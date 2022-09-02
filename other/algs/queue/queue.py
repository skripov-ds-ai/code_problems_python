class Queue:
    def __init__(self):
        # инициализация хранилища данных
        self.q = []

    def enqueue(self, item):
        # вставка в хвост
        self.q.append(item)

    def dequeue(self):
        # выдача из головы
        if self.size() > 0:
            t = self.q.pop(0)
            return t
        return None
        # если очередь пустая

    def size(self):
        return len(self.q)
        # размер очереди
