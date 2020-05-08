# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

# 设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

class Solution:
    def fun2(self, prices):
        length =len(prices)
        profit = 0
        if length<=1:
            return profit
        for i in range(1,length):
            if prices[i]>prices[i-1]:
                profit += prices[i]-prices[i-1]
        return profit

    def maxProfit(self,prices):
        length =len(prices)
        if length<=1:
            return 0
        profit = 0
        i = 1
        while(i<length):
            if prices[i]>prices[i-1]:
                profit += prices[i]-prices[i-1]
            i+=1
        return profit

    def fun1(self, prices):
        def fun(self,prices,holdPrice,status):
            profit = 0

            if len(prices)==1 :
                if status ==0:
                    pass
                elif status == 1:
                    profit = prices[0] - holdPrice
                    # print(profit)
            else:
                if status == 0: 
                    profit1 = fun(self,prices[1:],prices[0],1) # 买
                    profit2 = fun(self,prices[1:],holdPrice,0) # 不动
                    if profit1>profit2:
                        profit = profit1
                    else:
                        profit = profit2
                elif status == 1:
                    profit1 = fun(self,prices[1:],holdPrice,1) # 不动
                    profit2 = 0
                    if prices[0]-holdPrice>0:
                        profit2 = fun(self,prices[1:],0,0)+prices[0]-holdPrice # 卖
                    if profit1>profit2:
                        profit = profit1
                    else:
                        profit = profit2
                
            return profit
        if len(prices)<=1 :
                return 0
        profit1 = fun(self,prices[1:],0,0)
        profit2 = fun(self,prices[1:],prices[0],1)
        if profit1>profit2:
            return profit1
        else:
            return profit2
    

if __name__ == '__main__':
    a =Solution()
    print(a.maxProfit([7,1,5,2,3,4]))

