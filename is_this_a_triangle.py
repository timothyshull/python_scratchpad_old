import unittest


def is_triangle(a, b, c):
    return a < b + c and b < a + c and c < b + a


class TestIsTriangle(unittest.TestCase):
    def test_all(self):
        self.assertEqual(is_triangle(1, 2, 2), True, "didn't work when sides were 1, 2, 2")
        self.assertEqual(is_triangle(7, 2, 2), False, "didn't work when sides were 7, 2, 2")
        self.assertEqual(is_triangle(1, 2, 3), False, "didn't work when sides were 1, 2, 3")
        self.assertEqual(is_triangle(1, 3, 2), False, "didn't work when sides were 1, 3, 2")
        self.assertEqual(is_triangle(3, 1, 2), False, "didn't work when sides were 3, 1, 2")
        self.assertEqual(is_triangle(5, 1, 2), False, "didn't work when sides were 5, 1, 2")
        self.assertEqual(is_triangle(1, 2, 5), False, "didn't work when sides were 1, 2, 5")
        self.assertEqual(is_triangle(2, 5, 1), False, "didn't work when sides were 2, 5, 1")
        self.assertEqual(is_triangle(4, 2, 3), True, "didn't work when sides were 4, 2, 3")
        self.assertEqual(is_triangle(5, 1, 5), True, "didn't work when sides were 5, 1, 5")
        self.assertEqual(is_triangle(2, 2, 2), True, "didn't work when sides were 2, 2, 2")
        self.assertEqual(is_triangle(-1, 2, 3), False, "didn't work when sides were -1, 2, 3")
        self.assertEqual(is_triangle(1, -2, 3), False, "didn't work when sides were 1, -2, 3")
        self.assertEqual(is_triangle(1, 2, -3), False, "didn't work when sides were 1, 2, -3")
        self.assertEqual(is_triangle(0, 2, 3), False, "didn't work when sides were 0, 2, 3")


if __name__ == '__main__':
    unittest.main()
