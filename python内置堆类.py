import heapq
h = []
h.append(1)
h.append(2)
h.append(8)
h.append(5)
h.append(0)
print(h)
# 最小堆
heapq.heapify(h)
print(h)

print(heapq.heappop(h))
print(heapq.heappop(h))