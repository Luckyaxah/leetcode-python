def partition(arr, l,r, p ):
    """
    若返回值左边界大于右边界，说明无等于区域
    """
    less = l-1
    more = r+1
    while l<more:
        if arr[l]<p:
            less+=1
            arr[less], arr[l] = arr[l], arr[less]
            l+=1
        elif arr[l]>p:
            more -=1
            arr[more], arr[l] = arr[l], arr[more]
        else:
            l+=1
    return less+1,more-1

if __name__ == "__main__":
    arr = [1,5,2,3,5,2,1,6]
    p1,p2 = partition(arr,0,len(arr)-1,4)
    print(p1,p2)