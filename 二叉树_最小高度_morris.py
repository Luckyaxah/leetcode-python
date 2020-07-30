import math
def f(head):
    cur = head
    mostRight = None
    curLevel = 0
    minHeight = math.inf
    while cur != None:
        mostRight = cur.left
        if mostRight != None:
            leftHeight = 1
            while mostRight.right != None and mostRight.right != cur:
                leftHeight += 1
                mostRight = mostRight.right
            if mostRight.right == None:
                # 第一次来到该节点
                curLevel += 1
                mostRight.right = cur
                cur = cur.left
                continue
            else:
                if mostRight.left == None:
                    minHeight = min(minHeight, curLevel)
                curLevel -= leftHeight
                mostRight.right = None
        else:
            curLevel += 1
        cur = cur.right
    finalRight = 1
    cur = head
    while cur.right != None:
        finalRight += 1
        cur = cur.right
    if cur.left == None and cur.right == None:
        minHeight = min(minHeight, finalRight)
    return minHeight