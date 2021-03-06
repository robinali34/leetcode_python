import unittest
from src.easy.best_time_to_buy_and_sell_stock_ii.solution import Solution

class TestMaxProfit(unittest.TestCase):
    def test_maxProfit(self):
        solution = Solution()
        self.assertEqual(7, solution.maxProfit([7,1,5,3,6,4]))
        self.assertEqual(4, solution.maxProfit([1,2,3,4,5]))
        self.assertEqual(0, solution.maxProfit([7,6,4,3,1]))


if __name__ == '__main__':
    unittest.main()
