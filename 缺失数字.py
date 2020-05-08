class Solution:
    def missingNumber(self, nums) -> int:
        len_n = len(nums)+1
        e_sum = (0+len_n-1)*len_n/2
        for i in nums:
            e_sum -= i
        return int(e_sum)

    def missingNumber1(self, nums):
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing

if __name__ == "__main__":
    a = Solution()
    print(a.missingNumber([9,6,4,2,3,5,7,0,1]))