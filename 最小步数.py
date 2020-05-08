def minStep(arr):
    for ele in arr:
        if(ele<=0):
            return -1
    length = len(arr)
    if length==0 or length>100:
        return -1
    if length <= 2:
        return 1
    endPos = length-1
    firstStep = 1
    while firstStep < length/2:
        count = 1
        minimalCount = length
        currentPos = firstStep
        while(currentPos < endPos):
            currentPos = currentPos + arr[currentPos]
            count += 1
        if minimalCount > count and currentPos == endPos:
            minimalCount = count
        firstStep += 1

    if minimalCount == length:
        minimalCount = -1
    return minimalCount

if __name__ == '__main__':
    import sys 
    for line in sys.stdin:
        a = line.split()
        print(minStep(list(map(int,a))))