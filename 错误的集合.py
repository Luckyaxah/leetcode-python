class Solution:
    def findErrorNums(self, nums):
        m = {}
        dup = -1
        missing = 1
        for n in nums:
            m[n] = m.get(n,0) +1
        for i in range(1, len(nums)+1):
            if i in m:
                if m.get(i) == 2:
                    dup = i
            else:
                missing = i
        return [dup, missing]
            