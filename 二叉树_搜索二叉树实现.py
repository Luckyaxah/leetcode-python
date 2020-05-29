# Ignas Lelys
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
    def search(self, element):
        node = self.root
        while node != None and node.value != None and node.value != element:
            if element < node.value:
                node = node.left
            else:
                node = node.right
        return node
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
    def delete(self, element):
            node = self.search(element)
            if node != None:
                return self.deleteNode(node)
            else:
                return None
    def deleteNode(self, nodeNeedToDelete):
        if nodeNeedToDelete != None:
            nodeToReturn = None
            if nodeNeedToDelete != None:
                if nodeNeedToDelete.left == None:
                    # 如果left不存在，直接用right替换
                    # transplat(a, b) b去替换a的环境，a断连出来返回
                    nodeToReturn = self.transplant(nodeNeedToDelete, nodeNeedToDelete.right)
                elif nodeNeedToDelete.right == None:
                    # 如果right不存在，直接用left替换
                    nodeToReturn = self.transplant(nodeNeedToDelete, nodeNeedToDelete.left)
                else:
                    # 找右树的最左节点（其实就是最小值节点）
                    successorNode = self.getMinimum(nodeNeedToDelete.right)
                    # 要使用successorNode替换删除的节点
                    if successorNode.parent != nodeNeedToDelete: # 如果不是要删的节点的直接左孩子
                        self.transplant(successorNode, successorNode.right)
                        successorNode.right = nodeNeedToDelete.right
                        successorNode.right.parent = successorNode
                    self.transplant(nodeNeedToDelete, successorNode)
                    successorNode.left = nodeNeedToDelete.left
                    successorNode.left.parent = successorNode
                    nodeToReturn = successorNode
                self.size -= 1
            return nodeToReturn
        return None
    def transplant(self, nodeToReplace, newNode):
        if nodeToReplace.parent == None:
            self.node = newNode
        elif nodeToReplace == nodeToReplace.parent.left: # 如果要替换的节点是他父节点的左孩子
            nodeToReplace.parent.left = newNode
        else:
            nodeToReplace.parent.right = newNode
        if newNode != None:
            newNode.parent = nodeToReplace.parent
        return newNode

    def getMinimum(self, node):
        while node.left != None:
            node = node.left
        return node
    
    def getKthNode(self, k):
        if self.size >= k:
            return None
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
      
if __name__ == "__main__":
    pass