def heapSort(arr, asec):
    if not arr and len(arr)<2:
        return
    for i in range(len(arr)-1, -1,-1):
        heapify(arr,i,len(arr), asec)
    heap_size = len(arr)
    arr[0], arr[heap_size-1] = arr[heap_size-1], arr[0]
    heap_size -= 1
    while heap_size>0:
        heapify(arr, 0, heap_size, asec)
        arr[0], arr[heap_size-1] = arr[heap_size-1], arr[0]
        heap_size -= 1

def heapify(arr, index, arr_size, asec):
    factor = 1 if asec==0 else -1
    left = index * 2+1
    while left<arr_size:
        if left+1<arr_size and factor* arr[left+1] < factor*arr[left]:
            smallest = left+1
        else:
            smallest = left
            
        if factor* arr[index] > factor* arr[smallest]:
            arr[index], arr[smallest] =  arr[smallest], arr[index]
            index = smallest
            left = index*2+1
        else:
            break

if __name__ == "__main__":
    a = [3,9,2,6,7,4,2,1]
    print(a)
    heapSort(a, 0)
    print(a)
