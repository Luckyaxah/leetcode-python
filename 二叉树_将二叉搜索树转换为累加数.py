# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return []
        self.t = 0
        def process(root):
            if not root:
                return 0
            process(root.right)
            root.val = root.val + self.t
            self.t = root.val
            process(root.left)
            return root.val 
        process(root)
        return root

if __name__ == "__main__":
    # root = TreeNode(5)
    # root.left = TreeNode(2)
    # root.right = TreeNode(13)
    root = TreeNode(2)
    root.right = TreeNode(3)
    root.left = TreeNode(0)
    root.left.left = TreeNode(-4)
    root.left.right = TreeNode(1)
    from 二叉树_打印二叉树 import printTree
    printTree(Solution().convertBST(root))