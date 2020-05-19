import random
def quickSort(arr):
    def process(arr, l, r):
        if l<r:
            swap(arr, l+random.randint(0,r-l+1), r)
            p1,p2 = partition(arr, l ,r)
            process(arr, l, p1-1)
            process(arr, p2+1, r)
    def swap(arr, l,r):
        arr[l], arr[r] = arr[r], arr[l]
    def partition(arr,l,r):
        less = l-1
        more = r+1
        p = arr[r]
        while l<more:
            if arr[l] < p:
                swap(arr, less+1, l)
                less+=1
                l+=1
            elif arr[l] == p:
                l += 1
            else:
                swap(arr, more-1, l)
                more -= 1
        return less+1, more-1
    process(arr, 0, len(arr)-1)

if __name__ == "__main__":
    a = [12,2,5,2,3,1,7,23,2]
    print(a)
    quickSort(a)
    print(a)