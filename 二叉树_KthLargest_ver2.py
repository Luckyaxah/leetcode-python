from queue import PriorityQueue
import heapq
class KthLargest:

    def __init__(self, k: int, nums):
        self.h = nums[:]        
        self.k = k
        # self.pq = PriorityQueue(maxsize=k)
        # for i in nums:
        #     self.addpq(i)

        heapq.heapify(self.h)
        k1 = len(nums)-k
        while k1>0:
            heapq.heappop(self.h)
            k1 -= 1

    def add(self, val: int) -> int:
        if len(self.h) < self.k:
            heapq.heappush(self.h, val)
            ret = heapq.heappop(self.h)
            heapq.heappush(self.h, ret)
            return ret
        temp = heapq.heappop(self.h)
        if temp < val:
            heapq.heappush(self.h, val)
            ret = heapq.heappop(self.h)
            heapq.heappush(self.h, ret)
            return ret
        heapq.heappush(self.h, temp)
        return temp


    # def addpq(self, val: int) -> int:
    #     if len(self.h) < self.k:
    #         return val
    #     else:
    #         temp = heapq.heappop(self.h)
    #         if temp < val:
    #             pass
    #         # heapq.heappush(self.h)
    #     return None
        
if __name__ == "__main__":
    k = 3
    l = [4,5,8,2]
    kthLargest = KthLargest(k, l)
    print(kthLargest.add(3))   # returns 4
    print(kthLargest.add(5))   # returns 5
    print(kthLargest.add(10))  # returns 5
    print(kthLargest.add(9))   # returns 8
    print(kthLargest.add(4))   # returns 8       

