"""
    法一：中序遍历中节点后一个节点就是后继节点
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None

def getSuccessorNode(self, node: TreeNode):
    if not node:
        return node
    if node.right:
        return getLeftMost(node.right)
    else:
        parent = node.parent
        while parent and parent.left != node:
            node = parent
            parent = node.parent
        return parent
def getLeftMost(node):
    if not node:
        return node
    while node.left:
        node = node.left
    return node



if __name__ == "__main__":
     pass