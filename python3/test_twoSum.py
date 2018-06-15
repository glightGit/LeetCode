import unittest
from twoSum import *


class TestTwoSumFunc(unittest.TestCase):
    """Test twoSum.py"""
    def test_twoSum(self):
        t = Solution()
        self.assertEquals([0,2], t.twoSum([2, 7, 11, 15], 13))


if __name__ == '__main__':
    unittest.main()