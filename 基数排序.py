def radixSort(arr, l, r, digit):
    """
    digit 最大的数有多少个十进制位
    bucket 辅助空间，有多少个数则准备多少个辅助空间v
    """
    radix = 10
    i = 0
    j = 0
    bucket = [0]*(r-l+1)
    for d in range(1, digit+1):
        count = [0]*radix
        for i in range(l, r+1): # 做词频统计
            j = getDigit(arr[i], d)
            count[j] += 1
        for i in range(1, radix): # 做了一次数组累加
            count[i] = count[i] + count[i-1]
        for i in range(r, l-1, -1): # 从右往左
            j = getDigit(arr[i], d) # 一定是最后位置
            bucket[count[j]-1]= arr[i]
            count[j] -=1
        i = l
        j = 0
        while i<= r:
            arr[i] = bucket[j]
            i += 1
            j += 1

def getDigit(num, d):
    return (num // 10**(d-1) )%10

if __name__ == "__main__":
    arr = [22,21,32,31,1,100]
    print(arr)
    radixSort(arr,0,len(arr)-1,3)
    print(arr)