class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        self.titl = 0
        def process(root):
            if not root:
                return 0
            left = process(root.left)
            right = process(root.right)
            sum_ = left + right + root.val
            self.titl += abs(left-right)
            return sum_
        if not root:
            return 0
        process(root)
        return self.titl

if __name__ == "__main__":
    head = TreeNode(1)
    head.left = TreeNode(2)
    head.right = TreeNode(3)
    print(Solution().findTilt(head))