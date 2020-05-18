def selectionSort(arr):
    if (not arr) or (len(arr)<2):
        return
    for i in range(len(arr)-1):
        min_index = i
        for j in range(i+1,len(arr)):
            min_index = j if arr[j] < arr[min_index] else min_index
        swap(arr,i,min_index)

def swap(arr,i,j):
    arr[i], arr[j] = arr[j], arr[i]
    
if __name__ == "__main__":
    a = [1,24,3,4,6,3,4,1]
    selectionSort(a)
    print(a)
