from 二叉树类 import TreeNode

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def helper(root):
            if not root:
                return None
            root.left, root.right =helper(root.right), helper(root.left)
            return root
        return helper(root)

if __name__ == "__main__":

    a = Solution()
    t = TreeNode([4,2,7,1,3,6,9])
    ret = a.invertTree(t)
    ret._print()