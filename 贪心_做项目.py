class Node:
    def __init__(self, p, c):
        self.p = p
        self.c = c

class NodeP(Node):
    def __lt__(self, other):
        return other.p < self.p
class NodeC(Node):
    def __lt__(self, other):
        return self.c < other.c

def findMaximizedCapital(k, W, profits, capital):
    from queue import PriorityQueue
    minCostq = PriorityQueue()
    maxProfitQ = PriorityQueue()

    for p,c in zip(profits, capital):
        minCostq.put(NodeC(p,c))

    for i in range(k):
        while (not minCostq.empty()):
            temp = minCostq.get()
            if temp.c > W:
                minCostq.put(temp)
                break
            maxProfitQ.put(NodeP(temp.p, temp.c))
        if maxProfitQ.empty():
            return W
        temp = maxProfitQ.get().p
        print(temp)
        W += temp
    return W

if __name__ == "__main__":
    k = 3
    W = 2
    profits =[5,1,7,9,400]
    capital = [3,7,1,6,100]
    print(findMaximizedCapital(k,W, profits, capital))
