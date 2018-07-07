class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        
        if len(digits) == 0:
            return []
        result = [""]
        for i in range(len(digits)):
            # print(dic[digits[i]])
            oldlen = len(result)
            newlen = len(dic[digits[i]])
            result = result * newlen
            for j in range(oldlen):
                for k in range(newlen):
                    result[k * oldlen + j] = result[k * oldlen + j] + dic[digits[i]][k]

        print(result)
        return result




if __name__ == '__main__':
    t = Solution()
    # t.lengthOfLongestSubstring("abcabcbb")
    t.letterCombinations("23")
     