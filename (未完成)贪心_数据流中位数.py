# def modifyTwoHeapsSize():
#     if maxHeap.qsize() == minHeap.qsize() +2:
#         minHeap.put(maxHeap.get())
#     elif minHeap.qsize() == maxHeap.qsize()+2 :
#         maxHeap.put(minHeap.get())


# def addNumber(num):
#     if maxHeap.empty() or num <= maxHeap.peek():
#         maxHeap.put(num)
#     else:
#         minHeap.add(num)
#     modifyTwoHeapsSize()

# def getMedian():
#     maxHeapSize = maxHeap.qsize()
#     minHeapSize = minHeap.qsize()
#     if maxHeapSize + minHeapSize == 0:
#         return
#     maxHeapHead = maxHeap.peek()
#     minHeapHead = minHeap.peek()
#     if ((maxHeapSize + minHeapSize) & 1) == 0:
#         return (maxHeapHead + minHeapHead) /2
#     return maxHeapHead if maxHeapSize > minHeapSize else minHeapHead
