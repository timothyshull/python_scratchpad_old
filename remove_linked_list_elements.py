import unittest


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        tmp = dummy
        while tmp:
            if tmp.next and tmp.next.val == val:
                tmp2 = tmp.next
                tmp.next = tmp.next.next
                del tmp2
            tmp = tmp.next
        return dummy.next


class TestRemoveLLElems(unittest.TestCase):
    def test_one(self):
        dummy = ListNode(0)
        tmp = dummy
        for x in range(1, 7):
            tmp.next = ListNode(x)
            tmp = tmp.next

        sol = Solution()
        sol.removeElements(dummy.next, 6)

        result = []
        tmp = dummy.next
        while tmp:
            result.append(tmp.val)
            tmp = tmp.next

        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_two(self):
        dummy = ListNode(0)
        tmp = dummy
        for x in range(1, 7):
            tmp.next = ListNode(x)
            tmp = tmp.next

        sol = Solution()
        sol.removeElements(dummy.next, 3)

        result = []
        tmp = dummy.next
        while tmp:
            result.append(tmp.val)
            tmp = tmp.next

        self.assertEqual(result, [1, 2, 4, 5, 6])


if __name__ == '__main__':
    unittest.main()
