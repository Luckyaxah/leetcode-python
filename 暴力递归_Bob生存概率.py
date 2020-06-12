# 左神开窍之题



def bob1(N, M, i, j, K):
    allP = 4**K
    live = process(N,M,i,j,K)
    gcd  = get_gcd(allP, live)
    return '%d / %d' %(live/gcd, allP/gcd)


def process(N, M, row, col, rest):
    if row<0 or row == N or col < 0 or col == M:
        return 0
    if rest == 0:
        return 1
    live = process(N, M, row-1, col, rest - 1)
    live += process(N, M, row+1, col, rest -1)
    live += process(N, M, row, col-1, rest -1)
    live += process(N, M, row, col+1, rest - 1)
    return live

def get_gcd(m,n):
    return m if n==0 else get_gcd(n, m%n)