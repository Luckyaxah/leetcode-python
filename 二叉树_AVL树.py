from 二叉树_搜索二叉树节点左旋右旋 import AbstractSelfBalancingBinarySearchTree

class AVLTree(AbstractSelfBalancingBinarySearchTree):
    def __init__(self, value, parent, left, right):
        self.height = None
        super().__init__(value, parent, left, right)

    def insert(self,element):
        newNode = super().insert(element)
        self.rebalance(newNode)
        return newNode


    def delete(self, element):
        deleteNode = super().search(element)
        if deleteNode != None:
            successorNode = super().delete(deleteNode)
            if successorNode != None:
                minimum = self.getMinimum(successorNode) if successorNode.right != None else successorNode
                self.recomputeHeight(minimum)
                self.rebalance(minimum)
            else:
                self.recomputeHeight(deleteNode.parent)
                self.rebalance(deleteNode.parent)
            return successorNode
        return None

    def rebalance(self, node):
        while node != None:
            parent = node.parent
            leftHeight = -1 if node.left == None else node.left.height
            rightHeight = -1 if node.right == None else node.right.height
            # 右树高度减去左树高度，要么是RR型，要么是RL型
            nodeBalance = rightHeight - leftHeight

            # rebalance(-2 means left)
            if nodeBalance == 2:
                if node.right.right != None:
                    node = self.avlRotateLeft(node)
                    break
                else:
                    node = self.doubleRotateRightLeft(node)
                    break
            elif nodeBalance == -2:
                if node.left.left != None:
                    node = self.avlRotateRight(node)
                    break
                else:
                    node = self.doubleRotateLeftRight(node)
            else:
                self.updateHeight(node)
            
            node = parent
    
    def avlRotateLeft(self,node):
        temp = super().rotateLeft(node)
        self.updateHeight(temp.left)
        self.updateHeight(temp)
        return temp

    def avlRotateRight(self,node):
        temp = super().rotateRight(node)
        self.updateHeight(temp.right)
        self.updateHeight(temp)
        return temp
    
    def doubleRotateRightLeft(self,node):
        node.right = self.avlRotateRight(node.rotateRight)
        return self.avlRotateLeft(node)

    def doubleRotateLeftRight(self, node):
        node.left = self.avlRotateLeft(node.left)
        return self.avlRotateRight(node)

    def recomputeHeight(self,node):
        while node != None:
            node.height = self.maxHeight(node.left, node.right) + 1
            node = node.parent

    def maxHeight(self, node1, node2):
        # return highter height of 2 ndoes
        if node1 != None and node2 != None:
            return node1.height if node1.height > node2.height else node2.height
        elif node1 == None:
            return node2.height if node2 != None else -1
        elif node2 == None:
            return node1.height if node1 != None else -1
        return -1

    def updateHeight(self, node):
        leftHeight = -1 if node.left == None else node.left.height
        rightHeight = -1 if node.right == None else node.right.height
        node.height = 1 + max(leftHeight, rightHeight)
