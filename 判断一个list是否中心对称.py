# 判断list是否为中心对称

def isSymertricList(l):
    len_ret = len(l)
    # if len_ret %2 != 1:
    #     return False
    for i in range(len_ret //2):
        if l[i] != l[len_ret-i-1]:
            return False
    return True

if __name__ == "__main__":
    print(isSymertricList([2, 3, 1, 3, 2]))
    print(isSymertricList([1, 2, 3, 4, 2, 4, 3]))
    print(isSymertricList([2, 3, 3, 2]))