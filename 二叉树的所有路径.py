# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from 二叉树类 import TreeNode

class Solution:
    def binaryTreePaths(self, root: TreeNode) :
        def helper(node):
            if not node:
                return []
            if not (node.left or node.right):
                return [str(node.val)]
            left_ret, right_ret = helper(node.left), helper(node.right)

            left_ret = list(map(lambda x: str(node.val)+'->' + str(x), left_ret))
            right_ret = list(map(lambda x: str(node.val)+'->' + str(x), right_ret))
            return  left_ret+right_ret
        return helper(root)

if __name__ == "__main__":
    a = Solution()
    t = TreeNode([1,2,3,None,5])
    print(a.binaryTreePaths(t))