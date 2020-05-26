def sortTopology(graph):
    from queue import Queue
    q = Queue()

    inMap = {}
    for node in graph.nodes.values():
        inMap[node] = node.inDegree
    
    for node in inMap:
        if inMap[node] == 0:
            q.put(node)
    result = []
    while not q.empty():
        node = q.get()
        result.append(node.value)
        for i in node.nexts:
            inMap[i] -= 1
            if inMap[i] == 0:
                q.put(i)
    return result 

    

if __name__ == "__main__":
    arr = [
        [-1,0,2],
        [-1,1,0],
        [-1,1,2],
        [-1,1,4],
        [-1,2,4],
        [-1,2,3],
        [-1,3,4]
    ]
    from 图 import listToGraph
    g = listToGraph(arr)
    print(sortTopology(g))