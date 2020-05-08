class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        length =len(nums)
        t = k%length
        for i in range(t):
            nums.insert(0,nums.pop())
    def rotate1(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        length =len(nums)
        t = k%length
        for i in range(t):
            pre = nums[length-1]
            for j in range(length):
                temp = nums[j]
                nums[j] = pre
                pre = temp
    def rotate2(self, nums, k):
        """
        环状替换
        """
        length =len(nums)
        t = k%length
        count = 0

        for i in range(length):
            current = i
            pre = nums[i]
            if count == length:
                break

            while 1:
                next1 = (current +t) % length
                temp = nums[next1]
                nums[next1] = pre
                pre = temp
                current = next1
                count += 1
                if  i  == current :
                    break


        
            

if __name__ == '__main__':
    a =Solution()
    nums =[1,2,3,4,5,6,7]
    print(nums)
    a.rotate2(nums,3)
    print(nums)