
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findMode(self, root: TreeNode):
        dic = {}
        if not root:
            return []
        def process(root):
            if not root:
                return
            process(root.left)
            if root.val in dic:
                dic[root.val] += 1
            else:
                dic[root.val] = 1
            process(root.right)
        process(root)
        ret = []
        max_count = max(list(dic.values()))
        for key, value in dic.items():
            if value == max_count:
                ret.append(key)
        return ret

    
if __name__ == "__main__":
    from 二叉树_打印二叉树 import printTree
    head = TreeNode(1)
    head.right = TreeNode(2)
    head.right.left = TreeNode(2)
    head.right.right = TreeNode(3)
    head.right.right.left = TreeNode(3)
    # head = TreeNode(0)
    # head.right = TreeNode(0)
    printTree(head)
    print(Solution().findMode(head))

                    
                


            