# 给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。
from 二叉树类 import TreeNode

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        def fun(root,cur_sum):
            if not root:
                return False
            cur_sum += root.val
            if cur_sum  == sum and not (root.left or root.right):
                return True
            # if cur_sum  > sum:
            #     return False
            return fun(root.left,cur_sum) or fun(root.right,cur_sum)
        return fun(root,0)

if __name__ == "__main__":
    a = Solution()
    t = TreeNode([5,4,8,11,None,13,4,7,2,None,None,None,1])
    print(a.hasPathSum(t, 22))
    t = TreeNode([1,2])
    print(a.hasPathSum(t, 1))
    t = TreeNode([-2,None,-3])
    print(a.hasPathSum(t, -5))
