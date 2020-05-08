class Solution:
    def permute(self, nums):
        i = 0
        while i<len(nums):
            print(nums)
            temp = nums[len(nums)-1]
            for j in reversed(range(1,len(nums))):
                nums[j]=nums[j-1]
            nums[0]=temp
            i += 1

        

if __name__ == "__main__":
    a = Solution()
    nums = [1,2,3]
    a.permute(nums)