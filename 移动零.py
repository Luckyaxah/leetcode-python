class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_n = len(nums)
        count_zeros = 0
        ind = 0
        while ind <len_n:
            if nums[ind] == 0:
                nums.pop(ind)
                len_n -= 1
                count_zeros += 1
            else:
                ind += 1
        nums += [0] * count_zeros

if __name__ == "__main__":
    a = Solution()
    nums = [0,1,0,3,12]
    a.moveZeroes(nums)
    print(nums)