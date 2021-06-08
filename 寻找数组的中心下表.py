class Solution:
    def pivotIndex(self, nums) -> int:
        left = 0
        l = len(nums)
        right = sum(nums)
        for ind, num in enumerate(nums):
            if ind > 0:
                left += nums[ind-1]
            right -= num
            print(left, right)
            if left == right:
                return ind
        return -1



print(Solution().pivotIndex([1, 7, 3, 6, 5, 6]))
print(Solution().pivotIndex([1, 2, 3]))
print(Solution().pivotIndex([2, 1, -1]))
