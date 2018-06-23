class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # # print substring from maxlen to 1
        # for subLen in range(len(s), 0, -1):
        #     # print("sub len " + str(subLen))
        #     for i in range(len(s) + 1 - subLen):
        #         # print(str(i) + ":" + str(i + subLen))
        #         # subSet = set(s[i:i + subLen])
        #         subSet = set()
        #         for c in s[i:i + subLen]:
        #             if c in subSet:
        #                 break
        #             else:
        #                 subSet.add(c)
        #         if len(subSet) == subLen:
        #             # print(s[i:i + subLen])
        #             # print("sub len " + str(subLen))
        #             return subLen

        
        # for subLen in range(len(s), 0, -1):
        #     # print("sub len " + str(subLen))
        #     dic = {}
        #     for i in range(len(s)):
        #         # add cur char to dictionary
        #         c = s[i]
        #         if c in dic:
        #             dic[c] = dic[c] + 1
        #         else:
        #             dic[c] = 1
        #         # remove unused char
        #         if i >= subLen:
        #             removeChar = s[i - subLen]
        #             dic[removeChar] = dic[removeChar] - 1
        #             if dic[removeChar] == 0:
        #                 del dic[removeChar]
        #         # check
        #         if i >= subLen - 1 and len(dic) == subLen:
        #             # print(s[i:i + subLen])
        #             # print("sub len " + str(subLen))
        #             return subLen
        # return 0

        if len(s) <= 1:
            return len(s)

        begin = 0
        end = 0
        maxLen = 1
        dic = {s[0]:1}
        while end < len(s) - 1:
            end = end + 1
            c = s[end]
            if c in dic:
                dic[c] = dic[c] + 1
                while len(dic) < end - begin + 1:
                    removeChar = s[begin]
                    dic[removeChar] = dic[removeChar] - 1
                    if dic[removeChar] == 0:
                        del dic[removeChar]
                    begin = begin + 1
            else:
                dic[c] = 1
                if end - begin + 1 > maxLen:
                    maxLen = end - begin + 1

        return maxLen


if __name__ == '__main__':
    t = Solution()
    t.lengthOfLongestSubstring("abcabcbb")
     