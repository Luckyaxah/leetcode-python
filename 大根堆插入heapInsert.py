def heapInsert(arr, index):
    """
    [0...index-1]已经是大根堆了
    O(logN)
    """
    while index != 0 and arr[index]>arr[(index-1)//2]:
        arr[index], arr[(index-1)//2] = arr[(index-1)//2],arr[index]
        index = (index-1) //2

if __name__ == "__main__":
    a = [8,4,6]
    a.append(5)
    print(a)
    heapInsert(a,len(a)-1)
    print(a)