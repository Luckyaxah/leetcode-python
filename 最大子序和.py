class Solution:
    def maxSubArray(self, nums) :
        max_sum = nums[0]
        cur_sum = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            if cur_sum < nums[i]:
                cur_sum = nums[i]
            max_sum = max(max_sum, cur_sum)

        return max_sum

if __name__ == "__main__":
    a = Solution()
    print(a.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
    # print(a.maxSubArray([-1]))