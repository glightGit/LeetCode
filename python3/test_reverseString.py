import unittest
from reverseString import *


class TestFunc(unittest.TestCase):
    """Test reverseString.py"""
    def test_reverseString(self):
        t = Solution()
        self.assertEqual("olleh", t.reverseString("hello"))


if __name__ == '__main__':
    unittest.main()