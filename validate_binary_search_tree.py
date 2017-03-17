import unittest


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        if root.left and root.left.val >= root.val:
            return False
        if root.right and root.right.val <= root.val:
            return False
        return self.isValidBST(root.left) and self.isValidBST(root.right)


class TestRemoveLLElems(unittest.TestCase):
    def test_one(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)

        self.assertEqual(Solution().isValidBST(root), True)

    def test_two(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)

        self.assertEqual(Solution().isValidBST(root), False)

    def test_three(self):
        root = None
        self.assertEqual(Solution().isValidBST(root), True)


if __name__ == '__main__':
    unittest.main()
