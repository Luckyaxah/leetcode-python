class Solution:
    def dominantIndex(self, nums) -> int:
        ind = 0
        _max = nums[0]
        for i in range(len(nums)):
            if nums[i] > _max:
                _max = nums[i]
                ind = i
        for i in range(len(nums)):
            if i == ind:
                continue
            if _max < nums[i] *2:
                return -1
        return ind


# class Solution(object):
#     def dominantIndex(self, nums):
#         m = max(nums)
#         if all(m >= 2*x for x in nums if x != m):
#             return nums.index(m)
#         return -1

# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/largest-number-at-least-twice-of-others/solution/zhi-shao-shi-qi-ta-shu-zi-liang-bei-de-zui-da-sh-8/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。