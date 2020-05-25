class TreeNode:
    def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None

def inOrderUnRecur(head):
    if not head:
        return
    l = []
    cur = head
    while l or  cur:
        if cur:
            l.append(cur)
            cur = cur.left
        else:
            cur = l.pop()
            print(cur.val)
            cur = cur.right
       


if __name__ == "__main__":
    a = TreeNode(1)
    a.left = TreeNode(2)
    a.left.left = TreeNode(4)
    a.left.right = TreeNode(5)
    a.right = TreeNode(3)
    a.right.left = TreeNode(6)
    a.right.right = TreeNode(7)
    inOrderUnRecur(a)
    # 4,2,5,1,6,3,7
