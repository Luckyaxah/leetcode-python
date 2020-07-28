import math
class Solution:
    def maximumProduct(self, nums) -> int:
        nums = sorted(nums)
        output1 = nums[0] * nums[1] * nums[-1]
        output2 = nums[-1] * nums[-2] * nums[-3]
        return output1 if output1 > output2 else output2

if __name__ == "__main__":
    nums = [1,2,3,4]
    print(Solution().maximumProduct(nums))