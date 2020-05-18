def smallSum(arr):
    if (not arr) or len(arr) <2:
        return 0
    def process(arr, l,r):
        if l==r:
            return 0
        mid = l+((r-l)>>1)
        return process(arr, l, mid) \
            + process(arr, mid+1,r) \
            + merge(arr, l ,mid, r)
    def merge(arr,l,m,r):
        i = 0
        p1 = l
        p2 = m+1
        ret = 0
        help_arr=[0] * (r-l+1)
        while p1<=m and p2<= r:
            if arr[p1]<arr[p2]:
                help_arr[i] = arr[p1]
                ret += arr[p1]*(r-p2+1)
                p1 += 1
            else:
                help_arr[i] = arr[p2]
                p2 += 1
            i += 1
        while p1<= m:
            help_arr[i] = arr[p1]
            i+= 1
            p1+=1
        while p2<=r:
            help_arr[i] = arr[p2]
            i+= 1
            p2+=1
        for i in range(l-r+1):
            arr[i+l] = help_arr[i]
        return ret
    return process(arr,0,len(arr)-1)



if __name__ == "__main__":
    a = [1,4,4,1,2]
    print(smallSum(a))