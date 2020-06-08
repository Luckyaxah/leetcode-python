from typing import List
class Solution:
    def minMoves1(self, nums: List[int]) -> int:
        size = len(nums)
        temp = nums[:]
        count = 0
        index = -1
        while sum(temp) != size*max(temp):
            for i in range(size):
                if temp[i] == max(temp):
                    index = i
                temp[i] += 1
            temp[index] -= 1
            count += 1
        return count 

    def minMoves2(self, nums: List[int]) -> int:
        temp = nums[:]
        size = len(nums)
        count = 0
        while True:
            maxNum = max(temp)
            helperNums = [maxNum-i for i in temp]
            if max(helperNums) == 0:
                break
            count += max(helperNums)
            for index in range(size):
                if helperNums[index] == 0:
                    index1 = index
                temp[index] = temp[index]+ max(helperNums)
            temp[index1] -= max(helperNums)
        return count

    def minMoves(self, nums: List[int]) -> int:
        """
        该方法基于以下思路：将除了一个元素之外的全部元素+1，等价于将该元素-1，
        因为我们只对元素的相对大小感兴趣。因此，该问题简化为需要进行的减法次数。
        """
        
        count = 0
        minNum = min(nums)
        for num in nums:
            count += num-minNum
        return count 

if __name__ == "__main__":
    a = [1,21234]
    print(Solution().minMoves1(a))
    print(Solution().minMoves2(a))
    print(Solution().minMoves(a))