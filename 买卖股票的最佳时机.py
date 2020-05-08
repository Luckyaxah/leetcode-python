"""
如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。
"""
class Solution:
    def maxProfit(self, prices) -> int:
        max_profit = 0
        p = 0
        for i in range(len(prices)-1):
            if prices[i]<prices[p]:
                max_profit = max(prices[i+1]-prices[i],max_profit)
                p = i
            else:
                max_profit = max(prices[i+1]-prices[p],max_profit)
        return max_profit



if __name__ == "__main__":
    a = Solution()
    print(a.maxProfit(
        [7,1,5,3,6,4]
    ))
    print(a.maxProfit(
        [1,2]
    ))
    print(a.maxProfit(
        [2,1,2,1,0,1,2]
    ))
