import unittest
from src.medium.rotate_array.solution import Solution

class TestRotate(unittest.TestCase):

    def test_rotate(self):
        solution = Solution()
        nums = [1,2,3,4,5,6,7]
        solution.rotate(nums, 3)
        self.assertEqual([5,6,7,1,2,3,4], nums)
        nums = [-1,-100,3,99]
        solution.rotate(nums, 2)
        self.assertEqual([3,99,-1,-100], nums)

    def test_rotate1(self):
        solution = Solution()
        nums = [1,2,3,4,5,6,7]
        solution.rotate1(nums, 3)
        self.assertEqual([5,6,7,1,2,3,4], nums)
        nums = [-1,-100,3,99]
        solution.rotate1(nums, 2)
        self.assertEqual([3,99,-1,-100], nums)


if __name__ == '__main__':
    unittest.main()
