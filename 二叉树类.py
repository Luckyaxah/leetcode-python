# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        if type(x) == list:
            temp = TreeNode.list2TreeNode(x)
            self.val = temp.val
            self.left = temp.left
            self.right = temp.right
        else:
            self.val = x
            self.left = None
            self.right = None

    @classmethod
    def list2TreeNode(cls,tree_list):
        def fun(tree_list,ind):
            if not tree_list[ind]:
                return None
            ret = TreeNode(tree_list[ind])
            if ind*2+1 < len(tree_list):
                ret.left = fun(tree_list,ind*2+1)
            if ind*2+2 < len(tree_list):
                ret.right = fun(tree_list,ind*2+2)
            return ret
        return fun(tree_list,0)
         
    def _print(self):
        # 层序遍历
        p = []
        def fun(root):
            print(root.val)
            if root.left:
                p.append(root.left)
            if root.right:
                p.append(root.right)
            if not p:
                return
            fun(p.pop(0))
        fun(self)

    # def _print1(self):
    #     # 层序遍历
    #     p = []
    #     def fun(root):
    #         if not root :
    #             print(None)
    #         else:
    #             print(root.val)
    #             if root.left:
    #                 p.append(root.left)
    #             else:
    #                 p.append(None)
    #             if root.right:
    #                 p.append(root.right)
    #             else:
    #                 p.append(None)

    #         if not p:
    #             return
    #         fun(p.pop(0))
    #     fun(self)


if __name__ == "__main__":
    # x = TreeNode([1,2,3,None,None,4,5])
    # x._print()
    # print(x,type(x))
    # print(x.val,x.left.val,x.right.val,x.left.left.val)
    x = TreeNode([1,2,3,None,None,4,5,None,None,None,None,6,None,None,None])
    x._print()

