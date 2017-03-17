import unittest


# TODO: check this
class CycleFinder(object):
    def __init__(self, num_vertices, edge_list):
        self._has_cycle = False
        self._adjacency_lists = [list() for _ in range(num_vertices)]
        self._visited = [False for _ in range(num_vertices)]
        for elem in edge_list:
            self._adjacency_lists[elem[0]].append(elem[1])

        for n in range(num_vertices):
            if not self._visited[n]:
                self._dfs(n)

    def _dfs(self, vertex):
        self._visited[vertex] = True
        for n in self._adjacency_lists[vertex]:
            if self._visited[n]:
                self._has_cycle = True
            else:
                self._dfs(n)

    def has_cycle(self):
        return self._has_cycle


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        return not CycleFinder(numCourses, prerequisites).has_cycle()


class TestRemoveLLElems(unittest.TestCase):
    def test_one(self):
        self.assertEqual(Solution().canFinish(2, [[1, 0], [0, 1]]), False)

    def test_two(self):
        self.assertEqual(Solution().canFinish(5, [[0, 1], [1, 2], [3, 4]]), True)


if __name__ == '__main__':
    unittest.main()
