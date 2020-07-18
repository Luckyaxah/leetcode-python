def process(n):
    if n<0:
        return 0
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    res = 0
    for leftNum in range(n):
        leftWays = process(leftNum)
        rightWays = process(n-1-leftNum)
        res += leftWays * rightWays
    return res

def numTrees(n):
    if n < 2:
        return 1
    dp = [0 for i in range(n+1)]
    dp[0] = 1
    for i in range(1, n+1):
        for j in range(1, i+1):
            dp[i] += dp[j-1] * dp[i-j]
    return dp[n]