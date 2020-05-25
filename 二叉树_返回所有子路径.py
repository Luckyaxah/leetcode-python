from 二叉树类 import TreeNode

class Solution:
    def pathSum(self, root, sum: int) -> int:
        def helper(root, rets):
            if not root:
                return []
            ret = [[root.val]]
            l = helper(root.left,rets)
            if l:
                ret+= [[root.val]+ item for item in l]
            r = helper(root.right,rets)
            if r:
                ret+= [[root.val]+ item for item in r]
            rets += ret
            return ret
        rets = []
        helper(root, rets)
        return rets



if __name__ == "__main__":
    a = Solution()
    t = TreeNode([10,5,-3,3,2,None,11])
    print(a.pathSum(t,8))
