
def printTree(head):
    print("Binary Tree:")
    printInOrder(head, 0, "H", 17)

def printInOrder(head, height, to, length):
    if not head:
        return
    printInOrder(head.right, height+1,"v", length)
    val = to + str(head.val) + to
    lenM = len(val)
    lenL = (length-lenM) // 2
    lenR = length - lenM -lenL
    val = getSpace(lenL) + val + getSpace(lenR)
    print(getSpace(height*length)+val)
    printInOrder(head.left, height+1, "^", length)

def getSpace(num):
    space = " "*num
    return space

if __name__ == "__main__":
    class Node:
        def __init__(self,x):
            self.val = x
            self.left = None
            self.right = None
    a = Node(1)
    a.left = Node(2)
    a.left.left = Node(4)
    a.left.right = Node(5)
    a.right = Node(3)
    a.right.left = Node(6)
    a.right.right = Node(7)
    printTree(a)

	


