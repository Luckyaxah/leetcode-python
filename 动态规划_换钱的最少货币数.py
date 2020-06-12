def waysdp(arr, aim):
    if arr == None or len(arr) == 0 or aim < 0:
        return 0
    N = len(arr)
    dp = [[0 for j in range(aim+1)] for i in range(N+1)]
    dp[N][0] = 1
    for i in range(N-1, -1, -1):
        for rest in range(aim+1):
            dp[i][rest] = dp[i+1][rest]
            if rest-arr[i]>=0:
                dp[i][rest] += dp[i][rest - arr[i]]
    return dp[0][aim]

print(waysdp([5,2,3,1],350))
