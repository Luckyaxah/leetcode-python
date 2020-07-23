class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        self.s = ""
        def process(root):
            if not root:
                return
            self.s += str(root.val)
            if root.left:
                self.s += '('
                process(root.left)
                self.s += ')'
            elif root.right:
                self.s += '()'
            if root.right:
                self.s += '('
                process(root.right)
                self.s += ')'
        process(t)
        return self.s
            

if __name__ == "__main__":
    t = TreeNode(1)
    t.left = TreeNode(2)
    t.left.right = TreeNode(4)
    t.right = TreeNode(3)
    print(Solution().tree2str(t))