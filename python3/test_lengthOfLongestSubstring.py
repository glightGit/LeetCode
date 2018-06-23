import unittest
# from lengthOfLongestSubstring import *
import lengthOfLongestSubstring
import imp
imp.reload(lengthOfLongestSubstring)
from lengthOfLongestSubstring import *

class TestFunc(unittest.TestCase):
    """Test lengthOfLongestSubstring.py"""
    def test_lengthOfLongestSubstring(self):
        t = Solution()
        # print(t.lengthOfLongestSubstring("abcabcbb"))
        self.assertEqual(3, t.lengthOfLongestSubstring("abcabcbb"))
        self.assertEqual(1, t.lengthOfLongestSubstring("bbbbb"))
        self.assertEqual(3, t.lengthOfLongestSubstring("pwwkew"))
        self.assertEqual(0, t.lengthOfLongestSubstring(""))


if __name__ == '__main__':
    unittest.main()