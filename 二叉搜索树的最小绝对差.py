class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import math
class Info:
    def __init__(self, max_, min_, miniabs):
        self.max_ = max_
        self.min_ = min_
        self.miniabs = miniabs
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        if not root:
            return 0
        def process(root):
            if not root:
                return 
            linfo = process(root.left)
            rinfo = process(root.right)
            if (not linfo) and (not rinfo):
                return Info(root.val, root.val, math.inf)
            elif linfo and rinfo:
                p1 = min(root.val - linfo.max_, linfo.miniabs)
                p2 = min(rinfo.min_ - root.val, rinfo.miniabs)
                miniabs = min(p1, p2)
                max_ = rinfo.max_
                min_ = linfo.min_
                return Info(max_, min_, miniabs)
            elif linfo and not rinfo:
                miniabs = min(linfo.miniabs, root.val-linfo.max_)
                max_ = root.val
                min_ = linfo.min_
                return Info(max_, min_, miniabs)
            elif (not linfo) and rinfo:
                miniabs = min(rinfo.miniabs, rinfo.min_ - root.val)
                max_ = rinfo.max_
                min_ = root.val
                return Info(max_, min_, miniabs)

        info = process(root)
        return info.miniabs

if __name__ == "__main__":
    head = TreeNode(1)
    head.right = TreeNode(3)
    head.right.left = TreeNode(2)
    print(Solution().getMinimumDifference(head))