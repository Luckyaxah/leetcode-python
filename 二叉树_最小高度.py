import math

def minHeight(node):
    if node == None:
        return 0
    return process(node)


def process(head):
    if head.left == None and head.right == None:
        return 1
    lH = math.inf
    rH = math.inf
    if head.left:
        lH = process(head.left)
    if head.right:
        rH = process(head.right)
    return min(lH, rH)+1