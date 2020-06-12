def bob2(M,N,i,j,K):
    dp = [ [[0 for k in range(K+1)] for j in range(M+2) ] for i in range(N+2)]
    for row in range(1, N+1):
        for col in range(1, M+1):
            dp[row][col][0] = 1

    for rest in range(1, K+1):
        for row in range(1, N+1):
            for col in range(1, M+1):
                dp[row][col][rest] = dp[row-1][col][rest-1]
                dp[row][col][rest] += dp[row+1][col][rest-1]
                dp[row][col][rest] += dp[row][col-1][rest-1]
                dp[row][col][rest] += dp[row][col+1][rest-1]
    
    allP = 4**K
    live = dp[i+1][j+1][K]
    gcd = get_gcd(allP, live)
    return '%d / %d' %(live/gcd, allP/gcd)

def get_gcd(m,n):
    return m if n==0 else get_gcd(n, m%n)