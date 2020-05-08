
class Solution:
    def containsDuplicate1(self, nums) -> bool:
        d = []
        for i in nums:
            if i in d:
                return True
            d.append(i)
        return False
    def containsDuplicate2(self, nums) -> bool:
        for i in range(len(nums)):
            if nums[i] in nums[i+1:]:
                return True
        return False
    def containsDuplicate(self, nums) -> bool:
        pre = None
        nums.sort()
        for i in nums:
            if i == pre:
                return True
            pre = i
        return False

if __name__ == "__main__":
    a = Solution()
    print(a.containsDuplicate([1,2,3,1]))
    print(a.containsDuplicate([1,2,3,4]))