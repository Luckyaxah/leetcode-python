class Node:
    def __init__(self, x, parent, left, right):
        self.value = x
        self.left = None
        self.right = None
        self.parent = None
    def isLeaf(self):
        return self.left == None and self.right == None

class AbstractBinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0
    def createNode(self, value, parent, left, right):
        return Node(value, parent, left, right)
    def insert(self, element):
        if self.root == None:
            self.root = self.createNode(element,None,None, None)
            self.size += 1
            return self.root
        insertParentNode = None
        searchTempNode = self.root
        while(searchTempNode != None and searchTempNode.value != None):
            insertParentNode = searchTempNode
            if element < searchTempNode.value:
                searchTempNode = searchTempNode.left
            else:
                searchTempNode = searchTempNode.right
        newNode = self.createNode(element, insertParentNode, None, None)
        if insertParentNode.value > newNode.value:
            insertParentNode.left = newNode
        else:
            insertParentNode.right = newNode
        self.size += 1
        return newNode

    def getKthNode(self, k) -> int:
        # 中序遍历
        s = []
        cur = self.root
        count = 0
        while (s or cur):
            if cur:
                s.append(cur)
                cur = cur.left
            else:
                cur = s.pop()
                count += 1
                if count == k:
                    return cur.value
                cur = cur.right
        return 


class KthLargest:

    def __init__(self, k: int, nums):
        self.tree = AbstractBinarySearchTree()
        self.k = k
        for num in nums:
            self.tree.insert(-num)

    def add(self, val: int) -> int:
        self.tree.insert(-val)
        ret =  self.tree.getKthNode(self.k) 
        if ret != None:
            return -1 * ret
        return None
        
if __name__ == "__main__":
    k = 3
    l = [4,5,8,2]
    kthLargest = KthLargest(k, l)
    print(kthLargest.add(3))   # returns 4
    print(kthLargest.add(5))   # returns 5
    print(kthLargest.add(10))  # returns 5
    print(kthLargest.add(9))   # returns 8
    print(kthLargest.add(4))   # returns 8       
