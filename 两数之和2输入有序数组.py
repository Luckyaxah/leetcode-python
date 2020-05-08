class Solution:
    """
    序列不是从0开始，而是从1开始的
    """
    def twoSum(self, nums, target):
        d = {}
        for i in range(len(nums)):
            if target - nums[i] in d:
                return [d[target-nums[i]],i+1]
            else:
                d[nums[i]] = i+1


if __name__ == "__main__":
    a = Solution()
    print(a.twoSum([2,7,11,15],9))