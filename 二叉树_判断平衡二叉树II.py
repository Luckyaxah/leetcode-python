from 二叉树类 import TreeNode

class Info:
    def __init__(self, isb, h):
        self.isb = isb
        self.h = h

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def process(root):
            if not root:
                return Info(True, 0)
            leftInfo = process(root.left)
            rightInfo = process(root.right)
            isb = leftInfo.isb and rightInfo.isb and (abs(rightInfo.h-leftInfo.h) <= 1)
            h = max(leftInfo.h, rightInfo.h)+1
            return Info(isb, h)
        ret = process(root)
        return ret.isb
        
if __name__ == "__main__":
    a = Solution()
    t = TreeNode([3,9,20,None,None,15,7])
    print(a.isBalanced(t))
    t = TreeNode([1,2,2,3,3,None,None,4,4])
    print(a.isBalanced(t))