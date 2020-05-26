def dijkstra(fromNode):
    # 返回最小距离dict
    # key表示从from出发到达的node
    distanceMap = {}
    distanceMap[fromNode] = 0
    selectedNodes = set()
    minNode = getMinDistanceAndUnselectedNode(distanceMap, selectedNodes)
    while minNode:
        distance = distanceMap.get(minNode)
        for edge in minNode.edges:
            toNode = edge.toNode
            if not toNode in distanceMap:
                distanceMap[toNode] = distance + edge.weight
            else:
                distanceMap[toNode] = min(distanceMap[toNode], distance + edge.weight)
        selectedNodes.add(minNode)
        minNode = getMinDistanceAndUnselectedNode(distanceMap, selectedNodes)

    return distanceMap

def getMinDistanceAndUnselectedNode(distanceMap, selectedNodes):
    import sys
    ret = None
    minValue = sys.maxsize
    for node in distanceMap:
        if node in selectedNodes:
            continue
        if minValue > distanceMap[node]:
            minValue = distanceMap[node]
            ret = node
    return ret


if __name__ == "__main__":
    a=[
        [1,1,2],
        [7,1,3],
        [10,1,4],
        [2,2,3],
        [5,3,4],
        [3,4,5],
        [20,3,5],
        [50,2,5]
    ]
    from 图 import listToGraph
    g = listToGraph(a)
    print(dijkstra(g.nodes[1]))


