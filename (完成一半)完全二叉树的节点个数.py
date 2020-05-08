# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    # 这个是二叉树的节点个数，没有用到完全二叉树的性质
    def countNodes(self, root):
        count = 0
        def fun(root,count):
            if not root:
                return 0
            print('val:',root.val)
            return 1+ fun(root.left,count)+ fun(root.right,count)
        return fun(root,count)



if __name__ == "__main__":
    a = Solution()
    b = TreeNode(1)
    b.left = TreeNode(2)
    b.right = TreeNode(3)
    b.right.left = TreeNode(4)
    b.right.right = TreeNode(5)
    c = TreeNode(1)

    print(a.countNodes(b))
    print(a.countNodes(c))