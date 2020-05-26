from 图 import Node
def bfs(node):
    if not node:
        return 
    from queue import Queue
    q = Queue()
    s = set() # 不让节点重复进队列
    q.put(node)
    s.add(node)
    while not q.empty():
        cur = q.get()
        print(cur.value)
        for nextNode in cur.nexts:
            if not nextNode in s:
                q.put(nextNode)
                s.add(nextNode)
if __name__ == "__main__":
    a =[
        [1,0,1],
        [1,0,2],
        [1,0,3],
        [1,1,2],
        [1,2,3],
        [1,1,4],
        [1,2,5],
    ]
    from 图 import listToGraph
    g = listToGraph(a)
    enter = g.nodes[0]
    bfs(enter)