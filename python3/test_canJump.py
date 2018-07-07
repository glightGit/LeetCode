import unittest
# from canJump import *
import canJump
import imp
imp.reload(canJump)
from canJump import *

class TestFunc(unittest.TestCase):
    """Test canJump.py"""
    def test_canJump(self):
        t = Solution()
        # print(t.canJump("abcabcbb"))
        self.assertTrue(t.canJump([2,3,1,1,4]))
        self.assertFalse(t.canJump([3,2,1,0,4]))
        self.assertTrue(t.canJump([2,0,0]))
        self.assertTrue(t.canJump([0]))

if __name__ == '__main__':
    unittest.main()