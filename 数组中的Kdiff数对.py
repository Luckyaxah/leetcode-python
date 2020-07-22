class Solution:
    def findPairs1(self, nums, k: int) -> int:
        if k == 0:
            nums1 = []
            nums2 = []
            for num in nums:
                if num in nums1:
                    if num not in nums2:
                        nums2.append(num)
                    continue
                else:
                    nums1.append(num)  
            return len(nums2)
        elif k > 0:
            nums1 = []
            for num in nums:
                if num in nums1:
                    continue
                else:
                    nums1.append(num)
            nums1.sort()
            count = 0
            for i in range(len(nums1)):
                for j in range(i+1, len(nums1)):
                    if nums1[j]-nums1[i] == k:
                        count += 1
                    elif j - i > k:
                        break      
            return count
        else:
            return 0

    def findPairs(self, nums, k: int) -> int:
        if k < 0:
            return 0
        if k == 0:
            return len(set([i for i in nums if nums.count(i)>=2]))
        cl = [i+k for i in nums]
        return len(set(cl)&set(nums))


if __name__ == "__main__":
    nums = [-1,1]
    k = 2
    print(Solution().findPairs(nums, k))