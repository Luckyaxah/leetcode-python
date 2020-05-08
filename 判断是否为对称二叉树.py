from 二叉树类 import TreeNode

class Solution:


    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        def fun(left,right):
            if (not left) and right:
                return False
            elif left and (not right):
                return False
            elif not (left and  right):
                return True
            if left.val != right.val:
                return False
            return fun(left.left,right.right) and fun(left.right,right.left)
        return fun(root.left,root.right)

    def isSymmetric1(self, root: TreeNode) -> bool:
        ret = []
        ret1 = []
        def fun(root):
            if not root:
                return 
            # fun(root.left)
            # ret.append(root.val)
            # fun(root.right)
            # 若想看到None
            ret.append(fun(root.left))
            ret.append(root.val)
            ret.append(fun(root.right))

        def fun1(root):
            if not root:
                return 
            # fun1(root.right)
            # ret1.append(root.val)
            # fun1(root.left)
            # 若想看到None
            ret1.append(fun1(root.right))
            ret1.append(root.val)
            ret1.append(fun1(root.left))

        # 中序遍历
        fun(root)
        fun1(root)
        print(ret)
        print(ret1)

        return ret == ret1

if __name__ == "__main__":
    a = Solution()
    t = TreeNode([1,2,2,3,4,4,3])
    print(a.isSymmetric(t))
    t = TreeNode([1,2,2,None,3,None,3])
    print(a.isSymmetric(t))

    t = TreeNode([1,2,2,2,None,2])
    print(a.isSymmetric(t))


