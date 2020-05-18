import random

def genRandomArr(arr_len,minInt = 0, maxInt = 10):
    arr=[]
    for i in range(arr_len):
        arr.append(random.randint(minInt,maxInt))
    return arr

if __name__ == "__main__":
    a = genRandomArr(5,minInt=0, maxInt=10)
    print(a)