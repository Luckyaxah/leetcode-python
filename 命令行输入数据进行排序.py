# import sys

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


# import sys 
# i = 0
# line = sys.stdin.readlines()
# print(line)

n = int(input())
arr = list(map(int, input().split()))
asec = int(input())
# for line in sys.stdin:
#     if i ==0:
#         size = int(line)
#     elif i== 1:
#         arr = list(map(int,line.split()))
#     elif i==2:
#         asec = int(line)
#     i+=1
#     if i==3:
#         break


# while i<=2:
#     if i ==0:
#         size = int(sys.stdin.readline())
#     elif i== 1:
#         arr = sys.stdin.readline()
#         arr = list(map(int,arr.split()))
#     else:
#         asec = int(sys.stdin.readline())
#     i+=1

# print(arr)
heapSort(arr, asec= asec)
print(' '.join(map(str,arr)))