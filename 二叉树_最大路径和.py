class Info:
    def __init__(self, sum_):
        self.headWalkToLeafMaxPathSum = sum_

def process(root):
    if not root:
        return None
    linfo = process(root.left)
    rinfo = process(root.right)
    p1 = 0
    p2 = 0
    p3 = root.value

    if linfo:
        p1 = root.value + linfo.headWalkToLeafMaxPathSum
    if rinfo:
        p2 = root.value + rinfo.headWalkToLeafMaxPathSum


    return Info(max(p1,p2,p3))

def maxPathSum(head):
    return process(head).headWalkToLeafMaxPathSum