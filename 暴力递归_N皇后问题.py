def num1(n):
    if n<1:
        return 0
    record = [None]*n # i行的皇后，放在了第几列

    return process1(0, record, n)

def process1(i, record, n):
    """
    record[0...i-1]是摆放好的，且之前摆放的皇后都达标
    返回值是摆完所有皇后，合理摆法有多少种
    注意最后一个皇后是n-1号皇后
    """
    if i == n:
        return 1
    res = 0
    for j in range(n):
        if isValid(record, i,j):
            record[i] = j
            res += process1(i+1, record, n)
    
    return res

def isValid(record, i, j):
    for k in range(i):
        if j == record[k] or (abs(record[k]-j) == abs(i-k)):
            return False
    return True

def num2(n):
    # 常数时间极其省，利用位运算加速
    if n<1 or n>32:
        return 0
    limit = -1 if n==32 else ( (1<<n)-1 )
    return process2(limit, 0, 0, 0)

def process2(
    limit, 
    # 之前放过的所有皇后的列限制、左下对角线限制、右下对角线限制
    colLim, # 哪些列不能放皇后则标1，注意要在limit有效范围内
    leftDiaLim, # 左对角线限制，每下一行，左移动
    rightDiaLim # 右对角线限制，每下一行，右移动
    ):
    if colLim == limit: # 所有皇后全达标
        return 1
    # (colLim | leftDiaLim | rightDiaLim)总限制
    # 候选皇后的位置都在pos上了
    pos = limit & (~(colLim | leftDiaLim | rightDiaLim))
    res = 0
    while pos:
        mostRightOne = pos & (~pos+1) # 提取最右侧的1
        pos = pos - mostRightOne
        res += process2(
            limit,
            colLim | mostRightOne,
            (leftDiaLim | mostRightOne) <<1,
            (rightDiaLim | mostRightOne) >>1 # >>>是无符号右移, >>是有符号右移
            )
    return res
if __name__ == "__main__":
    m = 5
    print(num1(m))
    print(num2(m))

        

