arr = [3,1,2,5,2,4]

def fun1(arr):
    ret = []
    for i in range(len(arr)):
        left_ = arr[0]
        right_ = arr[-1]
        for j in range(i):
            if left_ < arr[j]:
                left_ = arr[j]
        for j in range(i+1,len(arr)):
            if right_ < arr[j]:
                right_ = arr[j]
        ret.append( max(min(right_,left_)-arr[i], 0) )
    return ret

print(fun1(arr))
print(sum(fun1(arr)))

def fun2(arr):
    L = 1
    R = len(arr) -2
    ret = 0
    l_max = arr[0]
    r_max = arr[len(arr)-1]
    while L<R:
        if l_max < r_max:
            if arr[L] < l_max:
                ret += l_max - arr[L]
                L += 1
            else:
                l_max = arr[L]
        else:
            if arr[R] < r_max:
                ret += r_max - arr[R]
                R -= 1
            else:
                r_max = arr[R]
    return ret
print(fun2(arr))