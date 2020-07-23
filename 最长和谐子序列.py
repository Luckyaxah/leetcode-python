class Solution:
    def findLHS(self, nums) -> int:
        """
        和谐数组是指一个数组里元素的最大值和最小值之间的差别正好是1。
        """
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        max_ = 0
        # print(d)
        for key in d.keys():
            # max_ = max(max_, d[key])
            if key+1 in d:
                max_ = max(max_, d[key]+d[key+1])
            # if key-1 in d:
            #     max_ = max(max_, d[key]+d[key-1])
        return max_

                

if __name__ == "__main__":
    nums = [1,3,2,2,5,2,3,7]
    print(Solution().findLHS(nums))