def primMST(graph):
    # 虽然有重复边的判断，但只影响常数时间
    from queue import PriorityQueue
    pq = PriorityQueue() # 存放边
    set1 = set()
    result = []
    for node in graph.nodes.values():
        if not node in set1:
            set1.add(node)
            for edge in node.edges:
                pq.put(edge)
            while not pq.empty():
                edge1 = pq.get()
                toNode = edge1.toNode
                if not toNode in set1:
                    set1.add(toNode)
                    result.append(edge1)
                    for new_edge in toNode.edges:
                        pq.put(new_edge)
    return result
def printSet(set1):
    for i in set1:
        print(i.weight, i.toNode, i.fromNode)

if __name__ == "__main__":
    a =[
        [1,1,4],
        [2,1,5],
        [7,1,2],
        [8,4,2],
        [3,2,5],
        [1,4,3],
        [10,3,5]
    ]
    from 图 import listToGraphUnoriented
    g = listToGraphUnoriented(a)
    ret = primMST(g)
    for edge in ret:
        print(edge.weight, edge.fromNode.value, edge.toNode.value)
