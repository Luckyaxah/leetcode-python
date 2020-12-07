class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        def process(head, val):
            if not head:
                return
            if head.val == val:
                return head
            if head.val > val:
                return process(head.left, val)
            if head.val < val:
                return process(head.right, val)
        return process(root, val)