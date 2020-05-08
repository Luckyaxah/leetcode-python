from 二叉树类 import TreeNode

class Solution:
    
    def isSameTree(self, p, q):
        def fun(p,q):
            if (not p) and q:
                return False
            elif  p and (not q):
                return False
            elif (not p) and (not q):
                return True
            if p.val != q.val:
                return False
            if fun(p.left,q.left) == False:
                return False
            if fun(p.right,q.right) == False:
                return False
            return True
        return fun(p,q)

if __name__ == "__main__":
    p = TreeNode([1,2,None,3])
    q = TreeNode([1,2,None,3])
    a = Solution()
    print(a.isSameTree(p,q))