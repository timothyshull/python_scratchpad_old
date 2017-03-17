import unittest


class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        idx1 = 0
        idx2 = 0
        idx3 = 0

        while idx1 < len(s1) and idx2 < len(s2) and idx3 < len(s3):
            res, idx1, idx2, idx3 = self.try_match(s1, s2, s3, idx1, idx2, idx3)
            if not res:
                return False

        return idx1 == len(s1) - 1 and idx2 == len(s2) - 1 and idx3 == len(s3) - 1

    # TODO: needs some sort of lookahead here
    @staticmethod
    def try_match(s1, s2, target, idx1, idx2, target_idx):
        res = False
        if s1[idx1] == target[target_idx] and s1[idx1 + 1] == target[target_idx]:
            idx1 += 1
            target_idx += 1
            res = True

        if s1[idx1] == target[target_idx]:
            idx1 += 1
            target_idx += 1
            res = True
        elif s2[idx2] == target[target_idx]:
            idx2 += 1
            target_idx += 1
            res = True
        return res, idx1, idx2, target_idx


class TestInterleave(unittest.TestCase):
    def test_one(self):
        self.assertEqual(Solution().isInterleave('aabcc', 'dbbca', 'aadbbcbcac'), True)

    def test_two(self):
        self.assertEqual(Solution().isInterleave('aabcc', 'dbbca', 'aadbbbaccc'), False)


if __name__ == '__main__':
    unittest.main()
