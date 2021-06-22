class TreeNode:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

def fun(root):
    ret = []
    ret1 = []
    def helper(node):
        if node is None:
            ret.append(None)
            return
        helper(node.left)
        helper(node.right)
        ret.append(node.value)
    def helper1(node):
        if node is None:
            ret1.append(None)
            return
        helper1(node.right)
        helper1(node.left)
        ret1.append(node.value)
    helper(root)
    helper1(root)
    print(ret)
    print(ret1)
    if ret == ret1:
        return True
    return False

left = TreeNode(2,None,TreeNode(3,None,None))
right = TreeNode(2,None, TreeNode(3,None,None))
root = TreeNode(1,left, right)

print(fun(root))