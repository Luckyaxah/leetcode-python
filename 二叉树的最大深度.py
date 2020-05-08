# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root):
        def fun(root):
            if not root:
                return 0
            if not root.left:
                return fun(root.right)+1
            if not root.right:
                return fun(root.left)+1
            return max( fun(root.left),fun(root.right))+1
        return fun(root)


if __name__ == '__main__':
    a = Solution()
    b = TreeNode(1)
    b.left = None
    b.right = TreeNode(2)
    b.right.left = TreeNode(3)
    ans = a.maxDepth(b)
    print(ans)

    # c = TreeNode(None)
    # ans = a.minDepth(c)
    # print(ans)