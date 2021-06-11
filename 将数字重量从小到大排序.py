class Solution:
    def sort(self , str ):
        def fun(s):
            d = int(s)
            sum = 0
            while d:
                sum += d % 10
                d = d // 10
            return sum
        nums = str.split(' ')
        # sorted 返回一个元组可以实现多级排序
        nums = sorted(nums, key=lambda x: (fun(x), x))
        return ' '.join(nums)

print(Solution().sort('91 19'))