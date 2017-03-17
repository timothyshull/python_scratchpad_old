import unittest


# 7 6 -> 6 + 5 * 7 or 5 + 6 * 6
# 8 6 -> 7 + 5 * 8 or 5 + 6 * 7
# 9 5 -> 8 + 9 * 4 or 4 + 5 * 8
def breakChocolate(n, m):
    if n > 0 and m > 0:
        return n - 1 + (n * (m - 1))
    else:
        return 0


class TestPersistence(unittest.TestCase):
    def test_all(self):
        self.assertEqual(breakChocolate(5, 5), 24)
        self.assertEqual(breakChocolate(1, 1), 0)


if __name__ == '__main__':
    unittest.main()
