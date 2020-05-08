class Solution:
    def singleNumber1(self, nums) -> int:
        t = []
        for i in range(len(nums)):
            if nums[i] in t:
                del t[t.index(nums[i])]
            else:
                t.append(nums[i])
        return t[0]
    def singleNumber2(self, nums) -> int:
        for i in range(len(nums)):
            if nums[i] in nums[i+1:]:
                del nums[i+1+nums[i+1:].index(nums[i])]
            else:
                return nums[i]
    def singleNumber(self, nums) -> int:
        a = 0
        for i in  nums:
            a ^= i
        return a

if __name__ == "__main__":
    a = Solution()
    print(a.singleNumber([2,2,1]))
    print(a.singleNumber([4,1,2,1,2]))
    print(a.singleNumber([1,4,2,1,2]))