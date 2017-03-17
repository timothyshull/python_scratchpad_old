import unittest


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def _inorder_r(self, root, out_list):
        if root:
            self._inorder_r(root.left, out_list)
            out_list.append(root.val)
            self._inorder_r(root.right, out_list)

    def inorderTraversalR(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        out_list = []
        self._inorder_r(root, out_list)
        return out_list

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        out_list = []
        stack = []
        tmp = root

        while tmp:
            while tmp:
                if tmp.right:
                    stack.append(tmp.right)
                stack.append(tmp)
                tmp = tmp.left

            tmp = stack.pop()

            while stack and not tmp.right:
                out_list.append(tmp.val)
                tmp = stack.pop()

            out_list.append(tmp.val)

            if stack:
                tmp = stack.pop()
            else:
                tmp = None
        return out_list


class TestInorderTraversal(unittest.TestCase):
    def test_one(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.left = TreeNode(3)

        self.assertEqual(Solution().inorderTraversal(root), [1, 3, 2])

    def test_two(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)

        self.assertEqual(Solution().inorderTraversal(root), [1, 2, 3])

    def test_three(self):
        root = None
        self.assertEqual(Solution().inorderTraversal(root), [])


if __name__ == '__main__':
    unittest.main()
