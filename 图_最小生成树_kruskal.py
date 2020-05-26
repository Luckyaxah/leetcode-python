
class MySets:
    # 这样的话isSameSet没法和union同时保持高效
    # 同时保持高效的集合是并查集
    def __init__(self, nodes):
        self.setMap = {}
        for cur in nodes:
            self.setMap[cur] = [cur]
    def isSameSet(self, node1, node2):
        return self.setMap[node1] == self.setMap[node2]
    def union(self, node1, node2):
        node1_list = self.setMap[node1] 
        node2_list = self.setMap[node2]
        for node in node2_list:
            node1_list.append(node)
            self.setMap[node] = node1_list # 注意这里是引用调用，不是值调用，很酷！

def kruskalMST(graph):
    from queue import PriorityQueue
    edges = list(graph.edges)
    query = MySets(graph.nodes.values())

    pq = PriorityQueue()

    for edge in edges:
        pq.put(edge)

    result = []
    while not pq.empty():
        edge = pq.get()
        if not query.isSameSet(edge.fromNode, edge.toNode):
            result.append(edge)
            query.union(edge.fromNode, edge.toNode)
    return result


if __name__ == "__main__":
    a =[
        [2,0,1],
        [1,0,3],
        [1,1,2],
        [2,2,3],
        [7,3,5],
        [1,5,6],
        [1,6,7],
        [1,7,8],
        [2,5,8],
        [3,4,8],
        [2,2,4]
    ]
    from 图 import listToGraphUnoriented
    g = listToGraphUnoriented(a)
    ret = kruskalMST(g)
    for edge in ret:
        print(edge.weight, edge.fromNode.value, edge.toNode.value)