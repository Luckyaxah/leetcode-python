class NumArray:

    def __init__(self, nums):
        self.sum = [0]
        len(nums)
        for i in nums:
            self.sum.append(self.sum[-1] + i)
        print(self.sum)

    def sumRange(self, i: int, j: int) -> int:
        return self.sum[j+1]-self.sum[i]
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

if __name__ == "__main__":
    a = NumArray([1,4,2,-3])
    print(a.sumRange(0,2))