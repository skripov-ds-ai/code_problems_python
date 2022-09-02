from unittest import TestCase
from bitarray import bitarray
from other.algs.bloom_filter.bloom_filter import BloomFilter

LEN = 10


class TestLBloomFilter(TestCase):
    def setUp(self) -> None:
        self.s = []
        for i in range(LEN):
            t = []
            for j in range(LEN):
                t.append((i + j) % LEN)
            t = "".join(map(str, t))
            self.s.append(t)

    def test_is_key(self):
        b = BloomFilter(32)
        b.add(self.s[0])
        self.assertTrue(b.is_value(self.s[0]))

    def test_is_key_false(self):
        b = BloomFilter(32)
        b.add(self.s[0])
        self.assertFalse(b.is_value(self.s[1]))

    def test_is_key_two_hash_equal(self):
        b = BloomFilter(32)
        # h1s = [b.hash1(s) for s in self.s]
        # h2s = [b.hash2(s) for s in self.s]
        # hs = list(sorted(enumerate(zip(h1s, h2s)), key=lambda x: (x[1][0], x[1][1], x[0])))
        # print(hs)
        b.add(self.s[0])
        self.assertTrue(b.is_value(self.s[2]))


