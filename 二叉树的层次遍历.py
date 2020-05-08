from 二叉树类 import TreeNode

class Solution:
    # def levelOrder(self, root):
    #     levels = []
    #     if not root:
    #         return levels
    #     def helper(node, level):
    #         # start the current level
    #         if len(levels) == level:
    #             levels.append([])

    #         # append the current node value
    #         levels[level].append(node.val)

    #         # process child nodes for the next level
    #         if node.left:
    #             helper(node.left, level + 1)
    #         if node.right:
    #             helper(node.right, level + 1)
            
    #     helper(root, 0)
    #     return levels

    def levelOrder(self, root) :
        levels = []
        if not root:
            return levels
        def fun(root,level):
            if len(levels) == level:
                levels.append([])
            levels[level].append(root.val)
            if root.left:
                fun(root.left,level+1)
            if root.right:
                fun(root.right,level+1)
        fun(root,0)
        return levels

    def myLevelOrder(self, root) :
        if not root:
            return [[]]
        ret = []
        def fun(root,level):
            if not root:
                return
            if len(ret)<level+1:
                ret.append([root.val])
            else:
                ret[level].append(root.val)
            fun(root.left,level+1)
            fun(root.right,level+1)
        fun(root,0)
        return ret


    # def _print(self):
    #     # 层序遍历
    #     p = []
    #     def fun(root):
    #         print(root.val)
    #         if root.left:
    #             p.append(root.left)
    #         if root.right:
    #             p.append(root.right)
    #         if not p:
    #             return
    #         fun(p.pop(0))
    #     fun(self)

if __name__ == "__main__":
    a = Solution()
    t = TreeNode([3,9,20,None,None,15,7])
    print(a.levelOrder(t))