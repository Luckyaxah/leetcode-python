from 二叉树类 import TreeNode

class Solution:
    def sumOfLeftLeaves(self, root) -> int:
        def helper(root,flag):
            if not root:
                return 0
            temp = 0
            if not (root.left or root.right) :
                if flag == 'left':
                    temp = root.val
            return temp + helper(root.left,'left') \
                + helper(root.right,'right')
        return helper(root,'left')

if __name__ == "__main__":
    a = Solution()
    t = TreeNode.list2TreeNode([3,9,20,1,None,15,7,10,11,None,None,2])
    print(a.sumOfLeftLeaves(t))