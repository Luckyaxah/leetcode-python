"""
    法一：中序遍历依次递增
    法二：二叉树递归套路
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Info:
    def __init__(self, nodes, height):  
        self.nodes = nodes
        self.height = height

class Solution:
    def isFull(self, root: TreeNode) -> bool:
        def process(x):
            if not x:
                return Info(0, 0)
            
            leftInfo = process(x.left)
            rightInfo = process(x.right)
            nodes = leftInfo.nodes+rightInfo.nodes+1
            height = max(leftInfo.height, rightInfo.height)+1
            return Info(nodes, height)
        ret = process(root)
        if ret.nodes == 2**ret.height-1:
            return True
        return False


if __name__ == "__main__":
    head = TreeNode(1)
    head.left = TreeNode(2)
    head.right = TreeNode(3)
    head.left.left = TreeNode(4)
    head.left.right = TreeNode(5)
    head.right.left = TreeNode(6)
    head.right.right = TreeNode(7)
    head.left.right.right = TreeNode(8)
    head.right.left.left = TreeNode(9)
    head.right.right.right = TreeNode(10)
    a = Solution()
    print(a.isFull(head))

    head = TreeNode(1)
    head.left = TreeNode(2)
    head.right = TreeNode(3)
    head.left.left = TreeNode(4)
    head.left.right = TreeNode(5)
    head.right.left = TreeNode(6)
    head.right.right = TreeNode(7)
    a = Solution()
    print(a.isFull(head))