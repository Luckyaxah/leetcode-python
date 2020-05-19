def heapify(arr, index, heapSize):
    """
    查看index是否能够下沉
    """
    left = index *2+1
    while left<heapSize:
        largest = left+1 \
            if left+1 < heapSize and arr[left+1] > arr[left] else left
        largest = largest if arr[largest] > arr[index] else index
        if largest == index:
            break
        arr[index],arr[largest]  = arr[largest] , arr[index]
        index = largest
        left = index *2 +1

if __name__ == "__main__":
    a = [5,9,8,4,6]
    print(a)
    heapify(a, 0, 5)
    print(a)