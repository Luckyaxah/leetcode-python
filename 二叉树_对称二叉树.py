class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        def fun(left,right):
            if (not left) and right:
                return False
            elif left and (not right):
                return False
            elif not (left and right):
                return True
            if left.val != right.val:
                return False
            return fun(left.left,right.right) and fun(left.right,right.left)
        return fun(root.left,root.right)