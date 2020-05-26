import functools
edges =[]
def mycmp(edge1,edge2):
    return edge1.weight-edge2.weight
# print(edges)
edges.sort(key=functools.cmp_to_key(mycmp))