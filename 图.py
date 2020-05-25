from typing import List, Dict, Set
class Node:
    def __init__(self, value:int, inDegree:int=0, outDegree:int=0, nexts:List[Node]=[], edges:List[Edge]=[]):
        self.value  = value
        self.inDegree = inDegree
        self.outDegree = outDegree
        self.nexts = nexts
        self.edges = edges

class Edge:
    def __init__(self, weight:int, fromNode: Node, toNode: Node):
        self.weight  = weight
        self.fromNode = fromNode
        self.toNode = toNode

class Graph:
    # 点集和边集
    # 这里edges应当是一个有序表HashMap，暂时使用Set[Edge]
    def __init__(self, nodes: Dict[int,Node]={}, edges: Set[Edge]=set()):
        self.nodes = nodes
        self.edges = edges
        
def listForm2Graph(matrix:List[List]):
    # a = [
    #     [7,0,1],
    #     [3,1,2],
    #     [5,0,2]
    # ]

    graph = Graph()
    for item in matrix:
        weight = item[0]
        fromNode = item[1]
        toNode = item[2]
        if not fromNode in graph.nodes:
            graph.nodes[fromNode] = Node(fromNode)
        if not toNode in graph.nodes:
            graph.nodes[toNode] = Node(toNode)
        fromNode = graph.nodes.get(fromNode)
        toNode = graph.nodes.get(toNode)

        newEdge = Edge(weight, fromNode, toNode) 
        fromNode.nexts.append(toNode)
        fromNode.outDegree += 1
        toNode.inDegree += 1
        fromNode.edges.append(newEdge)
        graph.edges.add(newEdge)