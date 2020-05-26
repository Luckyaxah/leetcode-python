from 图 import Node
def bfs(node):
    if not node:
        return 
    from queue import Queue
    q = []
    s = set() # 不让节点重复进栈
    q.append(node)
    s.add(node)
    print(node.value) # 入栈时打印
    while q:
        cur = q.pop()
        for nextNode in cur.nexts:
            if not nextNode in s:
                q.append(cur)
                q.append(nextNode)
                print(nextNode.value)
                s.add(nextNode)
                break
if __name__ == "__main__":
    a =[
        [-1,0,1],
        [-1,0,2],
        [-1,0,3],
        [-1,1,2],
        [-1,2,3],
        [-1,1,4],
        [-1,2,5],
    ]
    from 图 import listToGraph
    g = listToGraph(a)
    enter = g.nodes[0]
    bfs(enter)