class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # # pos = 0
        # path = [0] # jump path, start from pos 0
        # checkRecord = [0] * len(nums)
        # lastPos = len(nums) - 1

        # a = 1
        # while a == 1:
        #     pos = path[len(path) - 1]
        #     if nums[pos] + pos >= lastPos:
        #         return True
            
        #     nextPos = -1
        #     while checkRecord[pos] < nums[pos]:
        #         checkRecord[pos] = checkRecord[pos] + 1
        #         nextPos = pos + nums[pos] + 1 - checkRecord[pos]
        #         # if nextPos havent been checked
        #         if checkRecord[nextPos] < nums[nextPos]:
        #             break
        #         else:
        #             nextPos = -1
            
        #     if nextPos == -1:
        #         if pos <= 0:
        #             return False
        #         else:
        #             path.pop()
        #     else:
        #         path.append(nextPos)

        # if len(nums) <= 1:
        #     return True
        
        if len(nums) > 1 and nums[0] == 0:
            return False
            
        lastPos = len(nums) - 1
        pos = lastPos
        a = 1
        while a == 1:
            if pos <= 0:
                return True
            if nums[pos] > 0:
                pos = pos - 1
                # print(nums)
            else: # nums[pos] == 0
                p = pos - 1
                while p >= 0:
                    if pos == lastPos and nums[p] >= pos - p:
                        break
                    if pos != lastPos and nums[p] > pos - p:
                        break
                    p = p - 1
                if p >= 0:
                    pos = p
                    # while pos >= 0 and nums[pos] == 0:
                        # nums.pop()
                        # print(nums)
                        # pos = pos - 1
                else:
                    return False




if __name__ == '__main__':
    t = Solution()
    # t.lengthOfLongestSubstring("abcabcbb")
     