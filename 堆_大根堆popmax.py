from 大根堆的heapify import heapify
def popmax(arr, heap_size):
    """
    找到最大值返回，并删掉该值
    """
    t = arr[0]
    arr[0] = arr[heap_size-1]
    heap_size -= 1
    heapify(arr, 0, heap_size)
    return t


if __name__ == "__main__":
    a = [8,7,5,6,4,3]
    heap_size = len(a)
    print(a[:heap_size])
    print(popmax(a,len(a)))
    heap_size-=1
    print(a[:heap_size])
