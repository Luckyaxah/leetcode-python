def nodeNum(head):
    if head == None:
        return 0
    return bs(head, 1, mostLeftLevel(head, 1))

def bs(node, level, h):
    # h 整棵树最大深度
    # level 当前头节点在哪一层
    if level == h:
        return 1
    if mostLeftLevel(node.right, level+1) == h:
        return (1 << (h-level)) + bs(node.right, level+1, h)
    else:
        return (1 << (h-level -1)) + bs(node.left, level+1, h)

def mostLeftLevel(node, level):
    while node != None:
        level += 1
        node = node.left
    return level - 1