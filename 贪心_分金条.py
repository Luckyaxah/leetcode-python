def lessMoney(arr):
    from queue import PriorityQueue
    pq = PriorityQueue()
    for i in arr:
        pq.put(i)
    sum = 0
    cur = 0
    while pq.qsize() >1:
        cur = pq.get() + pq.get()
        sum += cur
        pq.put(cur)
    return sum

if __name__ == "__main__":
    nums = [6,3,2,9,13]
    print(lessMoney(nums))
