
def insertionSort(arr):
    for i in range(1,len(arr)):
        for j in range(i-1,-1,-1):
            if arr[j] >arr[j+1]:
                swap(arr,j,j+1)
            else:
                break

def swap(arr, i,j):
    arr[i],arr[j] = arr[j], arr[i]

if __name__ == "__main__":
    a = [1,24,3,4,6,3,4,1]
    insertionSort(a)
    print(a)