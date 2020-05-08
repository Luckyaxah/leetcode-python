# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。
class Solution:
    def permute(self, nums):
        def fun(nums):
            if not nums:
                return [[]]
            ret = []
            for i in range(len(nums)):
                first = nums[i]
                sub_nums = nums[:i]+nums[i+1:]
                t = fun(sub_nums)
                for j in range(len(t)):
                    t[j] = [first]+t[j]
                    ret.append(t[j])
            return ret
        return fun(nums)



if __name__ == "__main__":
    case1 = [0,1,2]
    # case2 = [0,1,2,3]
    a = Solution()
    print(a.permute(case1))
    # print(a.permute(case2))
    