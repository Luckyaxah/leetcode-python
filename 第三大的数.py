class Solution:
    def thirdMax(self, nums) -> int:
        maxQueue = [None]*3 
        for num in nums:
            i = 0
            while i < 3:
                if not maxQueue[i]:
                    maxQueue[i] = num
                    break
                if num == maxQueue[i]:
                    break
                if num > maxQueue[i]:
                    temp = maxQueue[i]
                    maxQueue[i] = num
                    num = temp
                i += 1
        if maxQueue[2]!=None and maxQueue[1] != maxQueue[2]:
            return maxQueue[2]
        return maxQueue[0]


if __name__ == "__main__":
    a = Solution()
    print(a.thirdMax([2,2,3,2,1]))