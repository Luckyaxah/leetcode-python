class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        def process(t1,t2):
            if not t1:
                return t2
            if not t2:
                return t1
            t1.val += t2.val
            t1.left = process(t1.left, t2.left)
            t1.right = process(t1.right,t2.right)
            return t1
        return process(t1,t2)

if __name__ == "__main__":
    from 二叉树_打印二叉树 import printTree
    t1 = TreeNode(1)
    t1.left = TreeNode(3)
    t1.left.left = TreeNode(5)
    t1.right = TreeNode(2)
    t2 = TreeNode(2)
    t2.left = TreeNode(1)
    t2.left.right = TreeNode(4)
    t2.right = TreeNode(3)
    t2.right.right = TreeNode(7)
    t = Solution().mergeTrees(t1,t2)
    printTree(t)