class Solution:
    def permuteUnique(self, nums):
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
                    if not is_include(ret,t[j]):
                        ret.append(t[j])

            return ret
        def is_include(ret,t):
            for i in ret:
                if i == t:
                    return True
            return False

        return fun(nums)


if __name__ == "__main__":
    case1 = [0,1,1]
    # case2 = [0,1,2,3]
    a = Solution()
    print(a.permuteUnique(case1))
    # print(a.permute(case2))