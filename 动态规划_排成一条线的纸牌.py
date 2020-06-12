# # f(L, R) 返回L--R范围内，先手能拿到的最高分数
# def f(arr, L, R):
#     if (L==R):
#         return arr[L]
#     return max(arr[L] + s(arr, L+1, R) ,arr[R] + s(arr, L, R-1) )

# def s(arr, L, R):
#     if L== R:
#         return 0
#     # 零和博弈，正数，你拿的少对手就拿的多
#     return min(f(arr, L+1,R), f(arr, L, R-1))


def windp(arr):
    N = len(arr)
    if arr == None or N == 0:
        return 0
    f = [[0 for i in range(N)] for j in range(N)]
    s = [[0 for i in range(N)] for j in range(N)]
    for i in range(N):
        f[i][i] = arr[i]
    # 0,0 右下方移动
    for col in range(1, N):
        # 对角线出发位置(0, col)
        L = 0
        R = col
        while L< N and R < N:
            f[L][R] = max(arr[L] + s[L+1][R] , arr[R]+s[L][R-1])
            s[L][R] = min(f[L+1][R], f[L][R-1])
            L += 1
            R += 1
    return max(f[0][N-1],s[0][N-1])
# print(f([3,7,100,20],0,3))
print(windp([5,7,4,5,8,1,6,0,3,4,6,1,7]))
print(windp([3,5,7,4,3]))