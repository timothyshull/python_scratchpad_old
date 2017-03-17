import unittest


def square_digits(num):
    out_str = ''
    for x in list(str(num)):
        out_str += str(int(x) ** 2)
    return int(out_str)
    # return int(''.join(str(int(d) ** 2) for d in str(num)))


class TestSquareDigits(unittest.TestCase):
    def test_one(self):
        self.assertEqual(square_digits(9119), 811181)

    def test_two(self):
        self.assertEqual(square_digits(4242), 164164)


if __name__ == '__main__':
    unittest.main()
