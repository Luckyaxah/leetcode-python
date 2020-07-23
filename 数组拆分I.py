class Solution:
    def arrayPairSum(self, nums) -> int:
        nums.sort()
        ret = 0
        for i in range(len(nums)//2):
            ret += nums[2*i]
            # print(nums[2*i], nums[2*i+1])
        return ret
        

if __name__ == "__main__":
    nums = [1,4,3,2]
    print(Solution().arrayPairSum(nums))