from typing import List, Dict, Set
class Node:
    def __init__(self, value:int):
        self.value  = value
        self.inDegree = 0
        self.outDegree = 0
        self.nexts = list()
        self.edges = list()

class Edge:
    def __init__(self, weight:int, fromNode: Node, toNode: Node):
        self.weight  = weight
        self.fromNode = fromNode
        self.toNode = toNode
    def __lt__(self,other_edge):
        return self.weight < other_edge.weight

class Graph:
    # 点集和边集
    # 这里edges应当是一个有序表HashMap，暂时使用Set[Edge]
    # 有序表所有操作O(logN)
    def __init__(self):
        self.nodes = {}
        self.edges = set()

def listToGraph(matrix:List[List]):
    # 转换为有向图
    graph = Graph()
    for item in matrix:
        weight = item[0]
        fromNodeValue = item[1]
        toNodeValue = item[2]
        if not fromNodeValue in graph.nodes:
            graph.nodes[fromNodeValue] = Node(fromNodeValue)
        if not toNodeValue in graph.nodes:
            graph.nodes[toNodeValue] = Node(toNodeValue)
        fromNode = graph.nodes.get(fromNodeValue)
        toNode = graph.nodes.get(toNodeValue)

        newEdge = Edge(weight, fromNode, toNode) 
        fromNode.nexts.append(toNode)
        fromNode.outDegree += 1
        toNode.inDegree += 1
        fromNode.edges.append(newEdge)
        graph.edges.add(newEdge)
    return graph


def listToGraphUnoriented(matrix:List[List]):
    # 转换为无向图
    graph = Graph()
    for item in matrix:
        weight = item[0]
        fromNodeValue = item[1]
        toNodeValue = item[2]
        if not fromNodeValue in graph.nodes:
            graph.nodes[fromNodeValue] = Node(fromNodeValue)
        if not toNodeValue in graph.nodes:
            graph.nodes[toNodeValue] = Node(toNodeValue)
        
        fromNode = graph.nodes.get(fromNodeValue)
        toNode = graph.nodes.get(toNodeValue)

        newEdge1 = Edge(weight, fromNode, toNode)
        newEdge2 = Edge(weight, toNode, fromNode)

        fromNode.nexts.append(toNode)
        toNode.nexts.append(fromNode)

        fromNode.outDegree += 1
        fromNode.inDegree = fromNode.outDegree
        toNode.inDegree += 1
        toNode.outDegree = toNode.inDegree
        
        fromNode.edges.append(newEdge1)
        toNode.edges.append(newEdge2)

        graph.edges.add(newEdge1)
        graph.edges.add(newEdge2)
    return graph


if __name__ == "__main__":
    a = [
        [7,0,1],
        [3,1,2],
        [5,0,2]
    ]
    g = listToGraph(a)
    