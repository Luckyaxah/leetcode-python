class Solution:
    def numSquares(self, n: int) -> int:
        # n <= 10^4
        nums = [num**2 for num in range(1, int(n**0.5)+1)]
        dp = [n for _ in range(n+1)]
        for num in nums:
            dp[num] = 1
        for num in nums:
            for i in range(num, n+1):
                dp[i] = min(dp[i], dp[i-num] + 1)

        # print(dp)
        return dp[n]
                
        

print(Solution().numSquares(12))

