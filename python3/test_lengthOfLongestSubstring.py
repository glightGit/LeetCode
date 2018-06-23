import unittest
from lengthOfLongestSubstring import *


class TestFunc(unittest.TestCase):
    """Test lengthOfLongestSubstring.py"""
    def test_lengthOfLongestSubstring(self):
        t = Solution()
        self.assertEqual(3, t.lengthOfLongestSubstring("abcabcbb"))
        self.assertEqual(1, t.lengthOfLongestSubstring("bbbbb"))
        self.assertEqual(3, t.lengthOfLongestSubstring("pwwkew"))


if __name__ == '__main__':
    unittest.main()