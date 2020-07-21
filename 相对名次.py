class Solution:
    def findRelativeRanks(self, nums):
        text = ['Gold Medal', 'Silver Medal', 'Bronze Medal']
        dic = {}
        for i in range(len(nums)):
            dic[nums[i]] = i
        temp = nums.copy()
        temp.sort(reverse=True)
        ret = nums.copy()
        for i in range(len(temp[:3])):
            ret[dic[temp[i]]] = text[i]
        if len(temp)>3:
            for i in range(3, len(temp)):
                ret[dic[temp[i]]] = str(i+1)
        return ret

if __name__ == "__main__":
    print(Solution().findRelativeRanks([5,4,3,2,1]))