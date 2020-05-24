class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isCBT(head):
    if not head:
        return
    from queue import Queue
    q = Queue()
    isMeet = False
    q.put(head)
    while not q.empty():
        cur = q.get()
        l = cur.left
        r = cur.right
        if (isMeet and (l !=None or r != None ))\
            or \
            (l==None and r !=None):
            return False
        if l:
            q.put(l)
        if r:
            q.put(r)
        if (not l) or ( not r):
            isMeet = True
    return True



if __name__ == "__main__":
    head = TreeNode(1)
    head.left = TreeNode(2)
    head.right = TreeNode(3)
    head.left.left = TreeNode(4)
    head.left.right = TreeNode(5)
    head.right.left = TreeNode(6)
    head.right.right = TreeNode(7)

    print(isCBT(head))