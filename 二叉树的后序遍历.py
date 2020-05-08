# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def postorderTraversal(self, root) :
        ret = []
        def fun(root):
            if not root:
                return
            fun(root.left)
            fun(root.right)
            ret.append(root.val)
        fun(root)
        return ret

if __name__ == '__main__':
    a = Solution()
    b = TreeNode(1)
    b.left = None
    b.right = TreeNode(2)
    b.right.left = TreeNode(3)
    c = TreeNode(None)
    ans = a.postorderTraversal(b)
    print(ans)
    ans = a.postorderTraversal(c)
    print(ans)