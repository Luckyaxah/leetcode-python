from 二叉树类 import TreeNode

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        def fun(root):
            if not root:
                return True, 0
            l_ret,l_level = fun(root.left)
            r_ret,r_level = fun(root.right)
            if l_ret and r_ret and (l_level -r_level<2 and l_level -r_level >-2):
                return True, max(l_level,r_level)+1
            return False, max(l_level,r_level)+1
        ret, level = fun(root)
        return ret
        
if __name__ == "__main__":
    a = Solution()
    t = TreeNode([3,9,20,None,None,15,7])
    print(a.isBalanced(t))
    t = TreeNode([1,2,2,3,3,None,None,4,4])
    print(a.isBalanced(t))