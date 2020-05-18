class Solution:
    def singleNumber(self, nums):
        eor = 0
        eor1 = 0
        for i in nums:
            eor ^= i

        rightOne = eor & (~eor+1)
        for i in nums:
            if i & rightOne!=0:
                eor1 ^= i
        return [eor1,eor1^eor]


if __name__ == "__main__":
    a = Solution()
    print(a.singleNumber([1,2,1,3,2,5]))