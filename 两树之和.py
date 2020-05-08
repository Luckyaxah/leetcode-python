class Solution:
    def twoSum1(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]
    def twoSum(self, nums, target):
        d = {}
        for i in range(len(nums)):
            if target - nums[i] in d:
                return [d[target-nums[i]],i]
            else:
                d[nums[i]] = i


if __name__ == "__main__":
    a = Solution()
    print(a.twoSum([2,7,11,15],9))