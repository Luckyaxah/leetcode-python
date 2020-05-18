class Solution:
    def sortArray(self, nums):
        """
        归并排序
        """
        def helper(nums,l,r):
            if l==r:
                return
            mid = l + ((r-l)>>1)
            helper(nums, l,mid)
            helper(nums, mid+1,r)
            merge(nums,l,mid,r)
        def merge(nums, l, m, r):
            help_arr=[0]*(r-l+1)
            p1 = l
            p2 = m+1
            i = 0
            while p1<=m and p2<=r:
                if nums[p1]<nums[p2]:
                    help_arr[i] = nums[p1]
                    p1+= 1
                else:
                    help_arr[i] = nums[p2]
                    p2+= 1  
                i+=1
            while p1<=m:
                help_arr[i] = nums[p1]
                i += 1
                p1 += 1
            while p2 <= r:
                help_arr[i] =  nums[p2]
                i += 1
                p2 += 1
            for i in range(r-l+1):
                nums[i+l] = help_arr[i]
        helper(nums,0,len(nums)-1)
        return nums
                    
    

if __name__ == "__main__":
    a = Solution()
    arr = [5,2,3,1]
    print(a.sortArray(arr))