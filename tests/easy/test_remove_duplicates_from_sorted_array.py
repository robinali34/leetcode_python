import unittest
from src.easy.remove_duplicates_from_sorted_array.solution import Solution

class TestRemoveDuplicates(unittest.TestCase):
    def test_removeDuplicates(self):
        solution = Solution()
        self.assertEqual(2, solution.removeDuplicates([1, 2, 2]))
        self.assertEqual(5, solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))


if __name__ == '__main__':
    unittest.main()
