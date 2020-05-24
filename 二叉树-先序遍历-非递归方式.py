class TreeNode:
    def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None

def preOrderUnRecur(head):
    if not head:
        return
    l = []
    l.append(head)
    while l:
        head = l.pop()
        print(head.val)
        if head.right:
            l.append(head.right)
        if head.left:
            l.append(head.left)

if __name__ == "__main__":
    a = TreeNode(1)
    a.left = TreeNode(2)
    a.left.left = TreeNode(4)
    a.left.right = TreeNode(5)
    a.right = TreeNode(3)
    a.right.left = TreeNode(6)
    a.right.right = TreeNode(7)
    preOrderUnRecur(a)
    # 1,2,4,5,3,6,7
