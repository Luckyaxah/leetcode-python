class Solution:
    def matrixReshape(self, nums, r: int, c: int):
        if r * c != len(nums)*len(nums[0]):
            return nums
        ret = [[None for j in range(c)] for i in range(r)]
        for ii in range(r):
            for jj in range(c):
                ret[ii][jj] = nums[(ii*c+jj)//len(nums[0])][(ii*c+jj)%len(nums[0])]
        return ret
if __name__ == "__main__":
    nums = [
        [1],[2],[3],[4]
    ]
    r = 2
    c = 2
    print(Solution().matrixReshape(nums, r, c))