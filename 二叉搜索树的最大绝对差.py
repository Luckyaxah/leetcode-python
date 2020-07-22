class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getMaximumDifference(self, root: TreeNode) -> int:
        if not root:
            return 0
        init = root.val
        def process(root):
            if not root:
                return init, init
            lmax, lmin = process(root.left)
            rmax, rmin = process(root.right)
            max_ = max(lmax, rmax)
            min_ = min(lmin, rmin)
            if root.val > max_:
                max_ = root.val
            if root.val < min_:
                min_ = root.val
            return max_, min_
        
        max_, min_ = process(root)
        return max_ - min_

if __name__ == "__main__":
    head = TreeNode(1)
    head.right = TreeNode(3)
    head.right.left = TreeNode(2)
    print(Solution().getMaximumDifference(head))