import math
class Info:
    def __init__(self, a, b, c, d):
        self.maxBSTSize = a
        self.isBST = b
        self.max = c
        self.min = d

def process(x):
    if x == None:
        return None
    leftInfo = process(x.left)
    rightInfo = process(x.right)

    maxVal = max( max(leftInfo.max if leftInfo else -math.inf,
    rightInfo.max if rightInfo else -math.inf ), x.val )

    minVal = min( min(leftInfo.min if leftInfo else math.inf,
    rightInfo.min if rightInfo else math.inf ), x.val )

    maxBSTSize = 0
    if leftInfo != None:
        maxBSTSize = max(maxBSTSize, leftInfo.maxBSTSize)
    if rightInfo != None:
        maxBSTSize =  max(maxBSTSize, leftInfo.maxBSTSize)

    isBST = False
    if (
        True if leftInfo == None else leftInfo.isBST
        and 
        True if rightInfo == None else rightInfo.isBST
        and 
        True if leftInfo == None else leftInfo.max<x.val
        and 
        True if rightInfo == None else rightInfo.min>x.val
    ):
        maxBSTSize = (0 if leftInfo== None else leftInfo.maxBSTSize) + \
        (0 if rightInfo== None else rightInfo.maxBSTSize) + 1


    return Info(maxBSTSize, isBST, maxVal, minVal)

if __name__ == "__main__":
    from 二叉树_打印二叉树 import printTree
    from 二叉树_序列化与反序列化 import Codec
    t_s = '5_2_1_#_#_3_#_#_8_7_#_#_10_#_#_'
    t = Codec().deserialize(t_s)
    printTree(t)

    print(process(t).maxBSTSize)

