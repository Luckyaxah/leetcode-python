# N: 1~N
# cur : 当前位置
# rest: 还剩rest步没走
# P: 最终目标位置是P
def ways1(N, start, K, P):
    if N<2 or K<1 or start<1 or start>N or P<1 or P>N:
        return 0
    return walk(N, start, K, P)

def walk(N, cur, rest, P):
    if rest == 0:
        return 1 if cur == P else 0
    if cur == 1:
        return walk(N, 2, rest-1, P)
    if cur == N:
        return walk(N, N-1, rest-1, P)
    return walk(N, cur+1, rest-1, P) + walk(N, cur-1, rest-1, P)

if __name__ == "__main__":
    print(ways1(5,2,4,4))