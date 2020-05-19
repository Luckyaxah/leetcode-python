# 对于一个无序数组A，请设计一个算法，求出需要排序的最短子数组的长度。
# 给定一个整数数组A及它的大小n，请返回最短子数组的长度。
from 堆排序 import heapSort

class Solution:
    def findUnsortedSubarray1(self, nums) -> int:
        nums1 = nums.copy()
        heapSort(nums)

        i = 0
        while i<len(nums):
            if nums[i] != nums1[i]:
                t1 = i
                break
            i+=1

        if i == len(nums):
            return 0
        j = len(nums)-1
        while j>-1:
            if nums[j] != nums1[j]:
                t2 = j
                break
            j -= 1
        return t2-t1+1

    def findUnsortedSubarray(self, nums) -> int:
        nums1 = nums.copy()
        nums.sort()

        i = 0
        while i<len(nums):
            if nums[i] != nums1[i]:
                t1 = i
                break
            i+=1

        if i == len(nums):
            return 0
        j = len(nums)-1
        while j>-1:
            if nums[j] != nums1[j]:
                t2 = j
                break
            j -= 1
        return t2-t1+1


    # def findShortest(self, A, n):
    #     # write code here
    #     high = 0
    #     low = 0
    #     B = A[:]
    #     for i in range(1,n):
    #         if A[i] < A[i - 1]:
    #             A[i],A[i-1] = A[i-1],A[i]
    #             high = i
                 
    #     for i in range(n - 1,0,-1):
    #         if B[i] < B[i - 1]:
    #             B[i],B[i-1] = B[i-1],B[i]
    #             low = i - 1
    #     if high == 0 and low == 0:
    #         return 0
    #     else:
    #         return high - low + 1

if __name__ == "__main__":
    a = Solution()
    nums = [2,6,4,8,10,9,15]
    print(a.findUnsortedSubarray(nums))
