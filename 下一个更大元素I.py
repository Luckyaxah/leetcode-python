class Solution:
    def nextGreaterElement1(self, nums1, nums2):
        ret = []
        for p in range(len(nums1)):
            temp = -1
            for t in range(len(nums2)):
                if nums2[t] == nums1[p]:
                    break
            for q in range(t+1, len(nums2)):
                if nums2[q] > nums1[p]:
                    temp = nums2[q]
                    break
            ret.append(temp)
        return ret

    def nextGreaterElement(self, nums1, nums2):
        hmap = {}
        mono_stack = []
        for num in nums2:
            if mono_stack and num > mono_stack[-1]:
                while mono_stack and num > mono_stack[-1]:
                    key = mono_stack.pop()
                    hmap[key] = num
            mono_stack.append(num)
        while mono_stack:
            key = mono_stack.pop()
            hmap[key] = -1
        ret = []
        for num in nums1:
            ret.append(hmap[num])
        return ret

        

if __name__ == "__main__":
    nums1 = [4,1,2]
    nums2 = [1,3,4,2]
    print(Solution().nextGreaterElement(nums1, nums2))
    print(Solution().nextGreaterElement([2,4], [1,2,3,4]))
