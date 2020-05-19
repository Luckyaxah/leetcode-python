def divide(arr, num):
    flag = -1
    for i in range(len(arr)):
        if arr[i]<= num:
            arr[flag+1], arr[i] = arr[i], arr[flag+1]
            flag += 1
        else:
            pass

if __name__ == "__main__":
    arr = [1,5,2,3,5,2,1,6]
    divide(arr,2)
    print(arr)