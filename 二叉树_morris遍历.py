# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# def process(head):
#     if head == None:
#         return 
#     # 1
#     # 先序 print(head.val)
#     process(head.left)

#     # 2
#     # 中序 print(head.val)

#     process(head.right)
#     # 后序 print(head.val)

#     # 3

def morris(head):
    if head == None:
        return
    cur = head
    mostRight = None
    while cur != None:
        mostRight = cur.left
        if mostRight != None:
            while mostRight.right != None and mostRight.right != cur:
                mostRight = mostRight.right
            if mostRight.right == None:
                # d
                mostRight.right = cur
                cur = cur.left
                continue
            else:
                mostRight.right = None
        cur = cur.right

def morrisPre(head):
    if head == None:
        return
    cur = head
    mostRight = None
    while cur != None:
        mostRight = cur.left
        if mostRight != None: # 可以来到自己两次的节点
            while mostRight.right != None and mostRight.right != cur:
                mostRight = mostRight.right
            if mostRight.right == None: 
                print(cur.val)
                mostRight.right = cur
                cur = cur.left
                continue
            else:
                mostRight.right = None
        else:
            # 只能来到自己一次的节点
            print(cur.val)
        cur = cur.right

def morrisIn(head):
    # 中序遍历
    if head == None:
        return
    cur = head
    mostRight = None
    while cur != None:
        mostRight = cur.left
        if mostRight != None: # 可以来到自己两次的节点
            while mostRight.right != None and mostRight.right != cur:
                mostRight = mostRight.right
            if mostRight.right == None: 
                mostRight.right = cur
                cur = cur.left
                continue
            else:
                print(cur.val)
                mostRight.right = None
        else:
            # 只能来到自己一次的节点
            print(cur.val)
        cur = cur.right

def morrisPos(head):
    # 后序遍历
    if head == None:
        return
    cur = head
    mostRight = None
    while cur != None:
        mostRight = cur.left
        if mostRight != None: # 可以来到自己两次的节点
            while mostRight.right != None and mostRight.right != cur:
                mostRight = mostRight.right
            if mostRight.right == None: 
                mostRight.right = cur
                cur = cur.left
                continue
            else:
                mostRight.right = None
                printEdge(cur.left)
        else:
            # 只能来到自己一次的节点
            pass
        cur = cur.right
    printEdge(head)

def printEdge(head):
    """
    以head为头的树，逆序打印该树右边界
    """
    tail = reverseEdge(head)
    cur = tail
    while cur != None:
        print(cur.val)
        cur = cur.right
    reverseEdge(tail)

def reverseEdge(fromNode):
    preNode = None
    nextNode = None
    while fromNode != None:
        nextNode = fromNode.right
        fromNode.right = preNode
        preNode = fromNode
        fromNode = nextNode
    return preNode


if __name__ == "__main__":
    b = TreeNode(1)
    b.left = None
    b.right = TreeNode(2)
    b.right.left = TreeNode(3)
    b.right.right = TreeNode(4)
    b.right.left.left = TreeNode(5)

    from 二叉树_打印二叉树 import printTree
    printTree(b)

    from 二叉树的前序遍历 import Solution
    ans = Solution().preorderTraversal(b)
    print(ans)
    morrisPre(b)

    from 二叉树的中序遍历 import Solution
    ans = Solution().inorderTraversal(b)
    print(ans)
    morrisIn(b)

    from 二叉树的后序遍历 import Solution
    ans = Solution().postorderTraversal(b)
    print(ans)
    morrisPos(b)




