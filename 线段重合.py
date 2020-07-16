import heapq
class Line:
    def __init__(self, start ,end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        return self.start < other.start

def maxCovers(start, end):
    # start和end都是列表，表示线段起终点
    if start == None or end == None or len(start) != len(end):
        return 0
    startMinHeap = []
    for i in range(len(start)):
        heapq.heappush(startMinHeap, Line(start[i], end[i]))
    # for i in startMinHeap:
    #     print(i.start, i.end)
    endMinHeap = []
    max_ = 0
    while startMinHeap:
        cur = heapq.heappop(startMinHeap)
        while endMinHeap and endMinHeap[0] <= cur.start:
            heapq.heappop(endMinHeap)
        heapq.heappush(endMinHeap, cur.end)
        max_ = max(max_, len(endMinHeap))
    return max_

if __name__ == "__main__":
    start =[1,1,1,2,5]
    end = [7,4,9,13,10]
    print(maxCovers(start, end))