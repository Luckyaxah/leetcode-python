def isCross(s1, s2, ai):
    if s1 == None or s2 == None or ai == None:
        return False
    str1 = list(s1)
    str2 = list(s2)
    aim = list(ai)
    if len(aim) != len(str1) + len(str2):
        return False
    dp = [[None for i in range(len(str1)+1)] for j in range(len(str2)+1)]
    dp[0][0] = True
    for i in range(1, len(str1)+1):
        if str1[i-1] != aim[i-1]:
            break
        dp[i][0] = True
    for j in range(1, len(str2)+1):
        if str2[j-1] != aim[j-1]:
            break
        dp[0][j] = True
    for i in range(1, len(str1)+1):
        for j in range(1, len(str2)+1):
            if (str1[i-1] == aim[i+j-1] and dp[i-1][j]) or \
                (str2[j-1] == aim[i+j-1] and dp[i][j-1]):
                dp[i][j] = True
    return dp[len(str1)][len(str2)]

s1 = 'abbc'
s2 = 'bbcd'
ai = 'abbbcbcd'
print(isCross(s1,s2,ai))