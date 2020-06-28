# 给定一个有序数组表示各店，给定一个L，代表L长的格子，问最多覆盖多少

def fun(arr, L):
    """
    两个循环遍历
    O(N^2)
    """
    count = 0
    max_count = -1
    for i in range(len(arr)):
        count = 0
        for j in range(i, len(arr)):
            if arr[i] + L > arr[j]:
                count += 1
        if count > max_count:
            index = i
            max_count = count
    return max_count, index

def fun1(arr, L):
    """
    O(NlogN)
    """
    max_count = -1
    for i in range(len(arr)):
        j = find_index(arr, i, L)
        if j>=0:
            count = i - j + 1
        else:
            count = 1
        if count > max_count:
            max_count = count
    return max_count

def find_index(arr, i, L):
    target = arr[i]-L
    l, r = 0, i-1
    j = -1
    while l <= r:
        mid = l + (r-l) //2
        if arr[mid] >= target:
            r = mid-1
            j = mid
        else:
            l = mid+1
    return j

def fun2(arr, L):
    """
    O(N)
    """
    l = 0
    r = 0
    max_count = -1
    for l in range(len(arr)):
        while r< len(arr) and arr[r] - arr[l] <= L:
            r += 1
        r -= 1
        count = r - l +1
        if count > max_count:
            max_count = count
    return max_count




if __name__ == "__main__":
    arr = [2,7,13,19,23,24,34]
    L = 8
    print(fun2(arr, L))