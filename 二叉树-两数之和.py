class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        def helper(root):
            if not root:
                return
            if root.val in d:
                return True
            d.append(k - root.val)
            ret1 = helper(root.left)
            ret2 = helper(root.right)
            return ret1 or ret2
        d = []
        return helper(root)