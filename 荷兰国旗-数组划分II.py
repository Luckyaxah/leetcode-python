def divide(arr, num):
    l_arr = -1
    r_arr = len(arr)
    i = 0
    while i<r_arr:
        if arr[i]< num:
            arr[l_arr+1], arr[i] = arr[i], arr[l_arr+1]
            l_arr += 1
            i+=1
        elif arr[i] == num:
            i+=1
        else:
            arr[r_arr-1], arr[i] = arr[i], arr[r_arr-1]
            r_arr -= 1



if __name__ == "__main__":
    arr = [1,5,2,3,5,2,1,6]
    divide(arr,5)
    print(arr)