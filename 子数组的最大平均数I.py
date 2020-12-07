class Solution:
    def findMaxAverage(self, nums, k: int) -> float:
        sums = [None for i in range(len(nums))]
        sums[0] = nums[0]
        for i in range(1, len(nums)):
            sums[i] = sums[i-1]+ nums[i]
        res = sums[k-1] / k
        for i in range(k, len(nums)):
            res = max(res, (sums[i]-sums[i-k])/k)
        return res
