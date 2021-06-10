class Solution:
    def change1(self, amount: int, coins) -> int:
        def dfs(amount, coins):
            if amount < 0:
                return 0
            if amount == 0:
                return 1
            if len(coins) == 0:
                return 0

            _max = amount // coins[0]
            count = 0
            for i in range(_max+1):
                count += dfs(amount - coins[0]*i, coins[1:])
            return count
        return dfs(amount, coins)

    def change(self, amount: int, coins) -> int:
        dp = [0 for i in range(amount+1)]
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] += dp[i-coin]
        return dp[amount]


print(Solution().change(5,[1,2,5]))
print(Solution().change(3,[2]))
print(Solution().change(10,[10]))