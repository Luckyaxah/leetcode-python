# 归并排序
def sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    arr1 = sort(arr[:mid])
    arr2 = sort(arr[mid:])
    t1 = 0
    t2 = 0
    ret = []
    while t1 < len(arr1) and t2 < len(arr2):
        if arr1[t1] <= arr2[t2]:
            ret.append(arr1[t1])
            t1 += 1
        else:
            ret.append(arr2[t2])
            t2 += 1
    while t1 < len(arr1):
            ret.append(arr1[t1])
            t1 += 1
    while t2 < len(arr2):
            ret.append(arr1[t2])
            t2 += 1
    return ret

temp = [5,2,6,4,8,2,3,1]
print(sort(temp))
         
        
