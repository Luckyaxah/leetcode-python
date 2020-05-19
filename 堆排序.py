def heapSort(arr):
    if not arr and len(arr)<2:
        return
    # O(NlogN)
    # for i in range(len(arr)):
    #     heapInsert(arr, i)
    # O(N)
    for i in range(len(arr)-1,-1,-1):
        heapify(arr,i,len(arr))
    print(arr)
    heap_size = len(arr)
    arr[0], arr[heap_size-1] = arr[heap_size-1], arr[0]
    heap_size -=1
    while heap_size >0:
        heapify(arr, 0, heap_size)
        arr[0], arr[heap_size-1] = arr[heap_size-1], arr[0]
        heap_size -=1

def heapInsert(arr, index):
    while index != 0 and arr[index]>arr[(index-1)//2]:
        arr[index], arr[(index-1)//2] = arr[(index-1)//2],arr[index]
        index = (index-1) //2

def heapify(arr, index, heap_size):
    left = 2*index+1
    while left< heap_size:
        if left+1<heap_size and arr[left+1]>arr[left]:
            largest = left+1
        else:
            largest = left
        largest = largest if arr[largest] > arr[index] else index
        if largest == index:
            break
        arr[index],arr[largest]  = arr[largest] , arr[index]
        index = largest
        left = index *2 +1


if __name__ == "__main__":
    a =[7, 6, 5, 3, 4, 3]
    print(a)
    heapSort(a)
    print(a)