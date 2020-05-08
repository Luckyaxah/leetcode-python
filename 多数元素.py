class Solution:
    def majorityElement1(self, nums) -> int:
        d ={}
        for num in nums:
            if num in d:
                d[num]+= 1
            else:
                d[num] = 1
        max_val = d[nums[0]]
        max_key = nums[0]
        for key,val in d.items():
            if val > max_val:
                max_val = val
                max_key = key
        return max_key

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        major = 0
        count = 0
        
        for n in nums:
            if count == 0:
                major = n
            if n == major:
                count = count + 1
            else:
                count = count - 1

        return major


if __name__ == "__main__":
    a = Solution()
    print(a.majorityElement([3,2,3]))