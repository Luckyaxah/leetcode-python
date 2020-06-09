def getNearLess(arr):
    """
    矩阵，List[List], 
    [
      0:[左边最近的索引，右边最近的索引],
      1:[左边最近的索引，右边最近的索引]
    ]
    -1表示不存在符合条件的索引
    """
    res = [[None]*2 for i in range(len(arr))]
    stack = [] # 存储索引，这个栈里的元素也是list
    for i in range(len(arr)):
        while stack and arr[stack[-1][0]] > arr[i]:
            popIs = stack.pop()
            leftLessIndex = -1 if not stack else stack[-1][-1]
            for popi in popIs:
                res[popi][0] = leftLessIndex
                res[popi][1] = i
        if stack and arr[stack[-1][0]] == arr[i]:
            stack[-1].append(i)
        else:
            l = []
            l.append(i)
            stack.append(l)
    while stack:
        popIs = stack.pop()
        leftLessIndex = -1 if not stack else stack[-1][-1]
        for popi in popIs:
            res[popi][0] = leftLessIndex
            res[popi][1] = -1
    return res
        

if __name__ == "__main__":
    l = [3,5,4,2,3,1,5]
    print(getNearLess(l))