class TreeNode:
    def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None

def posOrderUnRecur(head):
    if not head:
        return
    l = []
    l.append(head)
    l1 = []
    while l:
        head = l.pop()
        l1.append(head.val)
        # print(head.val)
        if head.left:
            l.append(head.left)
        if head.right:
            l.append(head.right)
    while l1:
        print(l1.pop())


if __name__ == "__main__":
    a = TreeNode(1)
    a.left = TreeNode(2)
    a.left.left = TreeNode(4)
    a.left.right = TreeNode(5)
    a.right = TreeNode(3)
    a.right.left = TreeNode(6)
    a.right.right = TreeNode(7)
    posOrderUnRecur(a)
    # 4,5,2,6,7,3,1
