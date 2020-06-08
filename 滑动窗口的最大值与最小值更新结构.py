def getMaxWindow(arr, w):
    if arr == None or w<1 or len(arr) < w:
        return None
    qmax = []
    res = [None]*(len(arr)-w+1)
    index = 0
    for i in range(len(arr)):
        while qmax and arr[qmax[-1]] <= arr[i]:
            qmax.pop()
        qmax.append(i)
        if qmax[0] == i-w:
            qmax.pop(0)
        if i>= w-1: # 说明窗口形成好了
            res[index] = arr[qmax[0]]
            index+= 1
    return res

def getMinWindow(arr, w):
    if arr == None or w<1 or len(arr) < w:
        return None
    qmax = []
    res = [None]*(len(arr)-w+1)
    index = 0
    for i in range(len(arr)):
        while qmax and arr[qmax[-1]] >= arr[i]:
            qmax.pop()
        qmax.append(i)
        if qmax[0] == i-w:
            qmax.pop(0)
        if i>= w-1:
            res[index] = arr[qmax[0]]
            index+= 1
    return res

if __name__ == "__main__":
    l = [3,4,1,2,6,4]
    print(getMaxWindow(l, 3))
    print(getMinWindow(l, 3))


