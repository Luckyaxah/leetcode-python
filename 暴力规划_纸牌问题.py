def win1(arr):
    def f(arr, i, j):
        if i==j:
            return arr[i]
        return max(
            arr[i] + s(arr, i+1, j),
            arr[j] + s(arr, i, j-1)
        )
    def s(arr, i, j):
        if i==j:
            return 0
        return min(
            f(arr, i+1, j),
            f(arr, i, j-1)
        )
    if (not arr) or (len(arr) == 0):
        return 0
    
    return max(f(arr,0,len(arr)-1), s(arr,0,len(arr)-1))

if __name__ == "__main__":
    l = [1,2,100,4]
    print(win1(l))