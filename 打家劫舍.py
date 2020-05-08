class Solution:
    # 递归一
    # def rob(self, nums) -> int:
    #     if not nums:
    #         return 0
    #     if len(nums)==1:
    #         return nums[0]
    #     if len(nums)==2:
    #         return max(nums[0],nums[1])
    #     return max(nums[0]+self.rob(nums[2:]),nums[1]+self.rob(nums[3:]))

    # 递归二
    # def rob(self, nums) -> int:
    #     if not nums:
    #         return 0
    #     if len(nums)==1:
    #         return nums[0]
    #     if len(nums)==2:
    #         return max(nums[0],nums[1])
    #     return max(self.rob(nums[:-1]),nums[-1]+self.rob(nums[:-2]))

    def rob(self, nums) -> int:
        choose_last, not_choose_last = 0, 0
        for num in nums:
            temp = not_choose_last + num
            not_choose_last = max(not_choose_last,choose_last)
            choose_last = temp
        return max(choose_last, not_choose_last)


if __name__ == "__main__":
    a = Solution()
    print(a.rob([1,2,3,1]))
    print(a.rob([2,7,9,3,1]))