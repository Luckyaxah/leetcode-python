class Solution:
    def removeElement(self, nums, val):
        i = 0
        length = len(nums)
        while True:
            if i == length:
                break
            if nums[i] == val:
                nums.pop(i)
                length -= 1
            else:
                i += 1
        return length

if __name__ == "__main__":
    a = Solution()
    print(a.removeElement([3,2,2,3],3))