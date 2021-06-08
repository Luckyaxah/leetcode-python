class Solution:
    def summaryRanges(self, nums):
        # 给定一个无重复元素的有序整数数组 nums
        # 返回 恰好覆盖数组中所有数字 的 最小有序 区间范围列表。
        # 也就是说，nums 的每个元素都恰好被某个区间范围所覆盖，并且不存在属于某个范围但不属于 nums 的数字 x 。
        # if len(nums)==1:
        #     return ["%d->%d"%(nums[0],nums[0]) ]
        if not nums:
            return []
        ret = []
        left = nums[0]
        right = left
        for num in nums[1:]:
            if num == right + 1:
                right = num
            else:
                if left == right:
                    ret.append("%d" % left)
                else:
                    ret.append("%d->%d"%(left,right))
                left = num
                right = left
        
        if left == right:
            ret.append("%d" % left)
        else:
            ret.append("%d->%d"%(left,right))
        return ret

print(Solution().summaryRanges([0,1,2,4,5,7]))
print(Solution().summaryRanges([0,2,3,4,6,8,9]))
print(Solution().summaryRanges([]))
print(Solution().summaryRanges([-1]))