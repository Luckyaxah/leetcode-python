from types import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ret = 0
        buy_price = prices[0]
        sell_price = prices[0]
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                sell_price = prices[i]
            elif prices[i] < prices[i-1] :
                if sell_price == prices[i-1]:
                    ret += sell_price - buy_price
                buy_price = prices[i]
        if sell_price == prices[-1]:
            ret += sell_price - buy_price 
        return ret

#     class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         profit = 0
#         for i in range(1, len(prices)):
#             tmp = prices[i] - prices[i - 1]
#             if tmp > 0: profit += tmp
#         return profit

# 作者：jyd
# 链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/solution/best-time-to-buy-and-sell-stock-ii-zhuan-hua-fa-ji/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。