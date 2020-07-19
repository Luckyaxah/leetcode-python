class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        max_ = 0
        temp = 0
        for i in nums:
            if i == 0:
                max_ = max(max_, temp)
                temp = 0
            else:
                temp += 1
        max_ = max(max_, temp)
        return max_