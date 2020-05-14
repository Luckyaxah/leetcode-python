class Solution:
    def findDisappearedNumbers1(self, nums) :
        if not nums:
            return []
        t = []
        num = max(nums)
        for j in range(1,num):
            if not j in nums:
                t.append(j)
        return t

    def findDisappearedNumbers2(self, nums) :
        if not nums:
            return []
        nums.sort()
        l = len(nums)
        t = []
        i = 1
        j = 0
        while j<l:
            if nums[j] == i:
                j+= 1
                i+= 1
            elif nums[j] < i:
                j += 1
            elif nums[j] > i:
                t.append(i)
                i += 1
        while i<=l:
            t.append(i)
            i+=1
        return t


    def findDisappearedNumbers3(self, nums) :
        if not nums:
            return []
        nums.sort()
        l = len(nums)
        nums1 = set(range(1,l+1))
        nums2 = set(nums)
        return list(nums1 -nums2)

    def findDisappearedNumbers(self, nums) :
        if not nums:
            return []
        l = len(nums)
        nums = set(nums)
        t = []
        for i in range(1,l+1):
            if not i in nums:
                t.append(i)
        return t






            

if __name__ == "__main__":
    a = Solution()
    print(a.findDisappearedNumbers([1,1]))
    print(a.findDisappearedNumbers([1,2,2,3]))
    print(a.findDisappearedNumbers([4,3,2,7,8,2,3,1]))