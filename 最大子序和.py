"""
连续子数组最大和
"""

class Solution:
    def maxSubArray(self, nums) :
        max_sum = nums[0]
        cur_sum = 0
        first = 0
        temp_first = 0
        last = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            if cur_sum < nums[i]:
                temp_first = i
                cur_sum = nums[i]
            if cur_sum > max_sum:
                first = temp_first
                last = i
                max_sum = cur_sum
        return max_sum, first, last

if __name__ == "__main__":
    a = Solution()
    print(a.maxSubArray([1, 2, 4, -2, -1, 2, 5, 2, -4, 1, -9, 2, -1]))
    # print(a.maxSubArray([-1]))