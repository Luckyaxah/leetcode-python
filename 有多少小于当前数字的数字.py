class Solution:
    def smallerNumbersThanCurrent(self, nums):
        ret = []
        nums1 = sorted(nums)
        d = {}
        for i, v in enumerate(nums1):
            if nums1[i] in d:
                continue
            else:
                d[nums1[i]] = i
        for i in nums:
            ret.append(d[i])
        return ret

