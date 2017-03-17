import unittest


def persistence(n):
    count = 0
    while True:
        current = 1
        decomp = list(str(n))
        if len(decomp) == 1:
            break
        for x in decomp:
            current *= int(x)
        n = current
        count += 1
    return count


# from operator import mul
#
#
# def persistence(n):
#     return 0 if n < 10 else persistence(reduce(mul, [int(i) for i in str(n)], 1)) + 1


class TestPersistence(unittest.TestCase):
    def test_all(self):
        self.assertEqual(persistence(39), 3)
        self.assertEqual(persistence(4), 0)
        self.assertEqual(persistence(25), 2)
        self.assertEqual(persistence(999), 4)


if __name__ == '__main__':
    unittest.main()
