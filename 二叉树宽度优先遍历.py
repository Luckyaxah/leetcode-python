class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def process(head):
    if not head:
        return
    from queue import Queue
    q = Queue()
    q.put(head)
    while not q.empty():
        cur = q.get()
        print(cur.val,end=" ")
        if cur.left:
            q.put(cur.left)
        if cur.right:
            q.put(cur.right)
        # print(q)
    print()



if __name__ == "__main__":
    head = TreeNode(1)
    head.left = TreeNode(2)
    head.right = TreeNode(3)
    head.left.left = TreeNode(4)
    head.left.right = TreeNode(5)
    head.right.left = TreeNode(6)
    head.right.right = TreeNode(7)

    process(head)