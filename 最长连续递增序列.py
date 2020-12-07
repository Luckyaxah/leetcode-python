class Solution:
    def findLengthOfLCIS(self, nums) -> int:
        if not nums:
            return 0
        count = 1
        ret = 1
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                count += 1
            else:
                ret = max(count, ret)
                count = 1
        ret = max(count, ret)
        return ret

