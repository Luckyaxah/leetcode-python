def mergeSort(arr):
    def helper(arr,l,r):
        if l == r:
            return
        mid = l + ((r-l)>>1)
        helper(arr, l,mid)
        helper(arr, mid+1,r)
        merge(arr, l,mid,r)
        pass
    def merge(arr, l,mid,r):
        help_arr = [0]*(r-l+1)
        i = 0
        p1 = l
        p2 = mid+1
        while p1<=mid and p2<=r:
            if arr[p1]<= arr[p2]:
                help_arr[i] = arr[p1]
                p1 += 1
            else:
                help_arr[i] = arr[p2]
                p2 += 1
            i+= 1
        while p1<=mid:
            help_arr[i] = arr[p1]
            i+=1
            p1+=1
        while p2<=r:
            help_arr[i] = arr[p2]
            i+=1
            p2+=1
        for i in range(r-l+1):
            arr[l+i] = help_arr[i]

    
    helper(arr, 0,len(arr)-1)
    

if __name__ == "__main__":
    a = [1,2,6,3,4,7,0,6,7]
    mergeSort(a)
    print(a)