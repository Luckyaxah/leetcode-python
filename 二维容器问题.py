import heapq

class Node:
    def __init__(self, value, r, c):
        self.value = value
        self.row = r
        self.col = c
    def __lt__(self, node):
        return self.value - node.value

def trapRainWater(heightMap):
    if heightMap == None or len(heightMap) == 0 or heightMap[0] == None or len(heightMap[0]) ==0:
        return 0
    N = len(heightMap)
    M = len(heightMap[0])
    isEnter = [[None for i in range(N)] for j in range(M)]
    heap = []
    for col in range(M):
        isEnter[0][col] = True
        heapq.heappush(heap, Node(heightMap[0][col], 0, col))
    for row in range(N):
        isEnter[row][M-1] = True
        heapq.heappush(heap, Node(heightMap[row][M-1], row, M-1))
    for col in range(M - 1, -1, -1):
        isEnter[N-1][col] = True
        heapq.heappush(heap, Node(heightMap[N-1][col], N-1, col))
    for row in range(N-1, -1, -1):
        isEnter[row][0] = True
        heapq.heappush(heap, Node(heightMap[row][0], row, 0))
    water = 0
    max_ = 0
    while heap:
        cur = heapq.heappop(heap)
        max_ = max(max_, cur.value)
        r = cur.row
        c = cur.col
        value = 0
        if r > 0 and not isEnter[r-1][c]:
            value = heightMap[r-1][c]
            water += max(0, max_ - value)
            isEnter[r-1][c] = True
            heapq.heappush(heap, Node(heightMap[r-1][c], r-1, c))
        if r < N-1 and not isEnter[r+1][c]:
            value = heightMap[r+1][c]
            water += max(0, max_ - value)
            isEnter[r+1][c] = True
            heapq.heappush(heap, Node(heightMap[r+1][c], r+1, c))
        if c > 0 and not isEnter[r][c-1]:
            value = heightMap[r][c-1]
            water += max(0, max_ - value)
            isEnter[r+1][c] = True
            heapq.heappush(heap, Node(heightMap[r+1][c], r+1, c))
        if c < M-1 and not isEnter[r][c+1]:
            value = heightMap[r][c+1]
            water += max(0, max_ -value)
            isEnter[r][c+1] = True
    return water