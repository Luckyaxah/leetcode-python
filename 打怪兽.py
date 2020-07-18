import math
def minMoney1(ability, money):
    # ability和money是正数数组
    if ability == None or len(ability) == 0 or money == None or len(money) == 0:
        return 0
    if len(ability) != len(money):
        return 0
    N = len(ability)
    sum_ = sum(ability)
    dp = [[-1 for i in range(N)] for j in range(sum_+1)]
    dp[0][ability[0]] = money[0]
    # 0列不需要管，都是-1
    for i in range(1, N):
        for j in range(1, sum_+1):
            if j<ability[i]:
                dp[i][j] = -1
            else: # j >= ability[i]
                p1 = dp[i-1][j]
                p2 = -1
                if dp[i-1][j-ability[i]] != -1:
                    p2 = dp[i-1][j-ability[i]] + money[i]
                
                if p1 == -1 or p2 == -1:
                    if p1 == -1:
                        dp[i][j] = p2
                    else:
                        dp[i][j] = p1
                else:
                    dp[i][j] = min(p1, p2)
    min_ = math.inf
    for j in range(sum_+1):
        if dp[N-1][j] != -1:
            min_ = min(min_, dp[N-1][j])
    return min_


def minMoney2(ability, money):
    if ability == None or len(ability) == 0 or money == None or len(money) == 0:
        return 0
    if len(ability) != len(money):
        return 0
    N = len(ability)
    sum_ = sum(money)
    dp = [[-1 for i in range(N)] for j in range(sum_+1)]
    # dp[i][j] 从0～i号怪兽，必须严格花j元，如果没有通过方案，则为-1
    # 如果有通过方案，则为所有通过方案中的最大能力值
    dp[0][money[0]] = ability[0]
    for i in range(1, N):
        for j in range(1, sum_+1):
            p1 = -1
            p2 = -1
            if dp[i-1][j] != -1 and dp[i-1][j] > ability[i]:
                p1 = dp[i-1][j]
            if j-money[i] >=0 and dp[i-1][j-money[i]] != -1:
                p2 = dp[i-1][j-money[i]] + ability[i]
            if p1 == -1 or p2 == -1:
                if p1 == -1:
                    dp[i][j] = p2
                else:
                    dp[i][j] = p1
            else:
                dp[i][j] = max(p1, p2)
    for j in range(sum_+1):
        if dp[N-1][j] != -1:
            return j
