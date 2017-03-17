import unittest


def likes(names):
    if not names:
        return 'no one likes this'
    elif len(names) == 1:
        return '{0} likes this'.format(names[0])
    elif len(names) == 2:
        return '{0} and {1} like this'.format(names[0], names[1])
    elif len(names) == 3:
        return '{0}, {1} and {2} like this'.format(names[0], names[1], names[2])
    else:
        return '{0}, {1} and {2} others like this'.format(names[0], names[1], len(names) - 2)


class TestLikes(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(likes([]), 'no one likes this')

    def test_one(self):
        self.assertEqual(likes(['Peter']), 'Peter likes this')

    def test_two(self):
        self.assertEqual(likes(['Jacob', 'Alex']), 'Jacob and Alex like this')

    def test_three(self):
        self.assertEqual(likes(['Max', 'John', 'Mark']), 'Max, John and Mark like this')

    def test_more(self):
        self.assertEqual(likes(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this')

if __name__ == '__main__':
    unittest.main()
