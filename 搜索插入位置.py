class Solution:
    def searchInsert(self, nums, target):
        len_nums = len(nums)
        for i in range(len_nums):
            if target <= nums[i]:
                    return i
        return len_nums

if __name__ == "__main__":
    a = Solution()
    print(a.searchInsert([1,3,5,6],5))
    print(a.searchInsert([1,3,5,6],2))