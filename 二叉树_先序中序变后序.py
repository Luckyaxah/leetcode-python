# def preAndInArrayToPosArray():
#     pre = []
#     L1 = None
#     R1 = None
#     in_ = []
#     L2 = None
#     R2 = None
#     pos = []
#     L3 = None
#     R3 = None
#     # 利用pre[L1..R1]和in_[L2..R2]生成pos[L3..R3]
def f(pre, l1, r1, in_, l2, r2, pos, l3, r3):
    if l1 > r1:
        return
    
    if l1 == r1:
        pos[l3] = pre[l1]
        
        # pre = ..[X ...]..
        # pos = ..[... X]..
        # in_ = ..[..X(?)..]..
    pos[r3] = pre[l1]
    found_ind = 0
    for i in range(l2, r2+1):
        if in_[i] == pre[l1]:
            found_ind = i
            break

    f(pre, l1+1, l1+found_ind-l2, in_, l2, found_ind-1,pos, l3, l3+found_ind-l2-1)
    f(pre, l1+found_ind-l2+1, r1, in_, found_ind+1, r2,pos, l3+found_ind-l2, r3-1)

    

def getPosArray(pre, in_):
    if pre == None or in_ == None:
        return None
    if len(pre) != len(in_):
        return None
    N = len(pre)
    pos = [None for i in range(N)]
    f(pre, 0, N-1, in_, 0, N-1, pos, 0, N-1)
    return pos


if __name__ == "__main__":
    pre = [1,2,4,5,3,6,7]
    in_ = [4,2,5,1,6,3,7]
    ret = getPosArray(pre, in_)
    print(ret)