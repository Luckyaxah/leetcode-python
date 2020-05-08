from 二叉树类 import TreeNode

class Solution:
    def levelOrderBottom(self, root: TreeNode) :
        if not root:
            return [[]]
        ret = []
        def fun(root,level):
            if not root:
                return
            if len(ret)<level+1:
                ret.append([root.val])
            else:
                ret[level].append(root.val)
            fun(root.left,level+1)
            fun(root.right,level+1)
        fun(root,0)
        return list(reversed(ret))


if __name__ == "__main__":
    a = Solution()
    t = TreeNode([3,9,20,None,None,15,7])
    print(a.levelOrderBottom(t))