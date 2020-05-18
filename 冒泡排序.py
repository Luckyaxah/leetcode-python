def bubbleSort(arr):
    if (not arr) or len(arr)<2:
        return
    for e in range(len(arr)-1,-1,-1):
        for i in range( e):
            if (arr[i] > arr[i+1]):
                swap(arr,i, i+1)
    
def swap(arr,i,j):
    arr[i] = arr[i] ^ arr[j]
    arr[j] = arr[i] ^ arr[j]
    arr[i] = arr[i] ^ arr[j]

if __name__ == "__main__":
    a = [1,24,3,4,6,3,4,1]
    bubbleSort(a)
    print(a)