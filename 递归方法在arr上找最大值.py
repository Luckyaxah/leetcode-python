def findMax(arr):
    if not arr:
        return
    def helper(arr, start, end):
        if (start == end):
            return arr[start]
        # 不推荐这个写法，因为有可能长度溢出，mid = (start+end)//2
        # mid = start+ (end-start)//2， //2相当于>>1
        mid = start + ((end-start) >> 1)
        leftMax = helper(arr,start, mid)
        rightMax = helper(arr,mid+1, end)
        return leftMax if leftMax>rightMax else rightMax
    return helper(arr, 0,len(arr)-1)
    

if __name__ == "__main__":
    a = [1,2,6,3,4,8,9,4,29,3,2,6,49,2,46]
    print(findMax(a))