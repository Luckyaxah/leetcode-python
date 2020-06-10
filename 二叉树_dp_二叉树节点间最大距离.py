class Info:
    def __init__(self, dis, h):
        self.maxDistance = dis
        self.height = h

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def process(x):
    # 以x为头的子树，返回要求的所有信息Info
    if x == None:
        return None
    leftInfo = process(x.left)
    rightInfo = process(x.right)
    maxDistance = 0
    height = max(leftInfo.height if leftInfo else 0, rightInfo.height if rightInfo else 0 ) + 1
    if leftInfo != None:
        maxDistance = leftInfo.maxDistance
    if rightInfo != None:
        maxDistance = max(maxDistance, rightInfo.maxDistance)
    
    maxDistance = max(maxDistance,
    (leftInfo.height if leftInfo else 0) + (rightInfo.height if rightInfo else 0) + 1
    )

    return Info(maxDistance, height)

if __name__ == "__main__":
    head1 = TreeNode(1)
    head1.left = TreeNode(2)
    head1.right = TreeNode(3)
    print(process(head1).maxDistance)