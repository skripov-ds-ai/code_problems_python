from bitarray import bitarray


class BloomFilter:
    def __init__(self, f_len):
        self.filter_len = f_len
        # создаём битовый массив длиной f_len ...
        self.f = bitarray(self.filter_len)
        self.f.setall(False)

    def __hash_fun(self, value, p):
        # в качестве value поступают строки!
        h = 0
        for v in value:
            h = (h * p + ord(v)) % self.filter_len
        return h

    def hash1(self, str1):
        # 17
        return self.__hash_fun(str1, 17)

    def hash2(self, str1):
        # 223
        return self.__hash_fun(str1, 223)

    def add(self, str1):
        t = self.hash1(str1)
        self.f[t] = True
        t = self.hash2(str1)
        self.f[t] = True
        # добавляем строку str1 в фильтр

    def is_value(self, str1):
        h1 = self.hash1(str1)
        h2 = self.hash2(str1)
        return self.f[h1] and self.f[h2]
        # проверка, имеется ли строка str1 в фильтре
