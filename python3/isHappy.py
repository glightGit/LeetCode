


class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        finish = False
        exists = set(str(n))
        while finish == False:
            sum = 0
            while n > 0:
                sum = sum + (n % 10) ** 2
                n = n // 10
            if sum == 1:
                return True
            strSum = str(sum)
            if strSum in exists:
                return False
            exists.add(strSum)
            n = sum
        


if __name__ == '__main__':
    t = Solution()
    print(t.isHappy(19))
