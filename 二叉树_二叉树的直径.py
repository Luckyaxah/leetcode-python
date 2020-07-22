# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Info:
    def __init__(self, height, max_diam):
        self.height = height
        self.max_diam = max_diam

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        """
        直径是任意两个节点最大值
        """
        def process(root):
            if not root:
                return Info(0,0)
            linfo = process(root.left)
            rinfo = process(root.right)
            height = max(linfo.height, rinfo.height)+1
            max_diam = max(linfo.height+1+rinfo.height, linfo.max_diam, rinfo.max_diam)
            return Info(height, max_diam)
        if not root:
            return 0
        info = process(root)
        return info.max_diam-1
        

if __name__ == "__main__":
    tree = TreeNode(1)
    tree.right = TreeNode(3)
    tree.left = TreeNode(2)
    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(5)
    print(Solution().diameterOfBinaryTree(tree))