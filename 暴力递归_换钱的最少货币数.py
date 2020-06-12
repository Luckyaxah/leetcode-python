def ways1(arr, aim):
    if arr == None or len(arr) == 0 or aim<0:
        return 0

    return process(arr, 0, aim)

def process(arr, index, rest):
    # 使用arr[index,...]之后的面值可以使用
    if index == len(arr):
        # 当此时无面值了，同时也不需要凑钱了
        return 1 if rest==0 else 0
    # 有面值的时候
    ways = 0
    zhang = 0
    while zhang * arr[index] <= rest:
        ways += process(arr, index+1, rest - zhang * arr[index])
        zhang += 1
    return ways

print(ways1([5,2,3],10))


