# 给定一个二叉树，返回它的中序遍历。
# 规则：若树为空，则空操作返回，否则从根节点开始（注意不是先访问根节点）中序遍历根节点的左子树，最后访问根节点
# 最后中序遍历右子树
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 解法一：
class Solution:
    def inorderTraversal(self, root) :
        result = []
        def fun(root):
            if not root:
                return 
            fun(root.left)
            result.append(root.val)
            fun(root.right)
        fun(root)
        return result



if __name__ == '__main__':
    a = Solution()
    b = TreeNode(1)
    b.left = None
    b.right = TreeNode(2)
    b.right.left = TreeNode(3)
    c = TreeNode(None)
    ans = a.inorderTraversal(b)
    print(ans)
    ans = a.inorderTraversal(c)
    print(ans)