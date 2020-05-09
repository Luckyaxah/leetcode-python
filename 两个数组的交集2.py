class Solution:
    def intersect(self, nums1, nums2) :
        ret = []
        for i in nums1:
            if i in nums2:
                ret.append(i)
                nums2.pop(nums2.index(i))
        return ret

if __name__ == "__main__":
    a = Solution()
    print(a.intersect([1,2,2,1,3], [2,3,3]))