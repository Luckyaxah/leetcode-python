class Solution:
    def merge(self, nums1, m, nums2 , n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i = 0
        j = 0
        while i < m+j and j<n:
            # print(i,j,nums1)
            if nums1[i]>nums2[j]:
                for t in reversed(range(i,m+j)):
                    nums1[t+1] = nums1[t]
                nums1[i]=nums2[j]
                j += 1
            i += 1
        if j < n:
            nums1[m+j:]=nums2[j:]

if __name__ == "__main__":
    a = Solution()
    nums1 = [1,2,3,0,0,0]
    nums2 = [2,5,6]
    a.merge(nums1,3,nums2,3)
    print(nums1)

    nums3 = [1]
    nums4 = []
    a.merge(nums3,1,nums4,0)
    print(nums3)
    nums3 = [2,0]
    nums4 = [1]
    a.merge(nums3,1,nums4,1)
    print(nums3)
    nums3 = [0]
    nums4 = [1]
    a.merge(nums3,0,nums4,1)
    print(nums3)

    nums3 = [1,0]
    nums4 = [2]
    a.merge(nums3,1,nums4,1)
    print(nums3)