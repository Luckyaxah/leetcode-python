class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        def process(root, val):
            if not root:
                return -1
            if root.val > val:
                return root.val
            l = process(root.left, val)
            r = process(root.right, val)
            if l>val and r>val:
                return min(l, r)
            return max(l, r)
        return process(root, root.val)