"""
    法一：中序遍历依次递增
    法二：二叉树递归套路
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Info:
    def __init__(self, isBst, min_v, max_v):  
        self.isBst = isBst
        self.min_v = min_v
        self.max_v = max_v
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def process(x):
            if not x:
                return 
            leftData = process(x.left)
            rightData = process(x.right)
            min_v = x.val
            max_v = x.val
            if leftData:
                min_v = leftData.min_v if min_v>leftData.min_v else min_v
                max_v = leftData.max_v if max_v<leftData.max_v else max_v
            if rightData:
                min_v = rightData.min_v if min_v>rightData.min_v else min_v
                max_v = rightData.max_v if max_v<rightData.max_v else max_v
            isBst = False
            if ( (leftData.isBst and leftData.max_v < x.val) if leftData else True) \
                and ((rightData.isBst and rightData.min_v > x.val) if rightData else True):
                isBst = True
            return Info(isBst, min_v, max_v)
        ret = process(root)
        return ret.isBst if ret else True


if __name__ == "__main__":
     pass