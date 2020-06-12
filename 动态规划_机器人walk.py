# f(cur,rest)
# N: 1~N
# cur : 当前位置
# rest: 还剩rest步没走
# P: 最终目标位置是P

# 使用了cache，傻缓存
def waysCache(N, start, K, P):
    if N<2 or K<1 or start<1 or start>N or P<1 or P>N:
        return 0
    cache = {}
    # key :2_3, value: v

    return f(N, start, K, P, cache)

# 当cur和rest确定了，返回值一定是确定的
def f(N, cur, rest, P, cache):

    key = '%s_%s' % (cur, rest)
    if key in cache:
        return cache[key]

    if rest == 0:
        cache[key] = 1 if cur == P else 0
        return cache[key]
    if cur == 1:
        cache[key] = f(N, 2, rest-1, P, cache)
        return cache[key]
    if cur == N:
        cache[key] = f(N, N-1, rest-1, P, cache)
        return cache[key]
    cache[key] = f(N, cur+1, rest-1, P, cache) + f(N, cur-1, rest-1, P, cache)
    return cache[key]

# 使用了cache，傻缓存
def waysCache2(N, start, K, P):
    if N<2 or K<1 or start<1 or start>N or P<1 or P>N:
        return 0
    # （cur, rest) cur范围1～N，rest范围0～k
    # 故缓存结构可以不需要使用hash表，可以使用二维数组。
    cache = [[-1 for j in range(K+1)] for i in range(N+1)]
    # 多准备了空间，0行不用

    return f2(N, start, K, P, cache)

# 当cur和rest确定了，返回值一定是确定的
def f2(N, cur, rest, P, cache):

    if cache[cur][rest] != -1:
        return cache[cur][rest] 

    if rest == 0:
        cache[cur][rest]  = 1 if cur == P else 0
        return cache[cur][rest] 
    if cur == 1:
        cache[cur][rest] = f2(N, 2, rest-1, P, cache)
        return cache[cur][rest]
    if cur == N:
        cache[cur][rest] = f2(N, N-1, rest-1, P, cache)
        return cache[cur][rest]
    cache[cur][rest] = f2(N, cur+1, rest-1, P, cache) + f2(N, cur-1, rest-1, P, cache)
    return cache[cur][rest]

# 使用了cache，傻缓存
def waysdp(N, start, K,end):
    if N<2 or K<1 or start<1 or start>N or end<1 or end>N:
        return 0
    # （cur, rest) cur范围1～N，rest范围0～k
    # 故缓存结构可以不需要使用hash表，可以使用二维数组。
    dp = [[0 for j in range(K+1)] for i in range(N+1)]
    dp[end][0] = 1
    for col in range(1, K+1):
        dp[1][col] = dp[2][col-1]
        dp[N][col] = dp[N-1][col-1]
        for row in range(2, N):
            dp[row][col] = dp[row-1][col-1]+dp[row+1][col-1]
    return dp[start][K]

if __name__ == "__main__":
    print(waysdp(5,2,4,4))