import math

def minCost2(s1, s2):
    ans = math.inf
    str2 = list(s2)
    for start in range(len(s1)):
        for end in range(start+1, len(s1)+1):
            ans = min(ans, distance(str2, list(s1[start:end])))
    return ans

def distance(str2, s1sub):
    row = len(str2)
    col = len(s1sub)
    dp = [[None for i in range(row)] for j in range(col)]
    # dp[i][j]表示
    # str2[0..i]仅通过删除行为编程s1sub[0..j]的最小代价
    # 可能性1:
    #    str2[0..i]变的过程中，不保留最后一个字符即，需要通过str[0..i-1]编导s1sub[0..j]
    #    dp[i][j] = dp[i-1][j]+1
    # 可能性2:
    #    str2[0..i]变的过程中，想保留最后一个字符，这要求str2[i] == s1sub[j]，然后str2[0..i-1]要变成s1sub[0..j-1]
    #    dp[i][j] = dp[i-1][j-1]
    dp[0][0] = 0 if str2[0] == s1sub[0] else math.inf
    for j in range(1, col):
        dp[0][j] = math.inf
    for i in range(1, row):
        dp[i][0] = i if dp[i-1][0] != math.inf or str2[i] == s1sub[0] else math.inf
    for i in range(1, row):
        for j in range(1, col):
            dp[i][j] = math.inf
            if dp[i-1][j] != math.inf:
                dp[i][j] = dp[i-1][j] + 1
            if str2[i] == s1sub[j] and dp[i-1][j-1] != math.inf:
                dp[i][j] = min(dp[i][j], dp[i-1][j-1])
    return dp[row-1][col-1]
