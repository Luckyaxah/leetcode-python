from 二叉树_搜索二叉树实现 import AbstractBinarySearchTree

class AbstractSelfBalancingBinarySearchTree(AbstractBinarySearchTree):

    def rotateLeft(self, node):
        temp = node.right # 当前节点的右节点
        temp.parent = node.parent 

        node.right = temp.left # 新节点的左支挂在原节点的右支上
        if node.right != None:
            node.right.parent = node

        temp.left = node
        node.parent = temp

        # temp took over node's place so now its parent should point to temp
        if temp.parent != None:
            if node == temp.parent.left:
                temp.parent.left = temp
            else:
                temp.parent.right = temp
        else:
            self.root = temp

        return temp

    def rotateRight(self, node):
        temp = node.left # 当前节点的右节点
        temp.parent = node.parent 

        node.left = temp.right # 新节点的左支挂在原节点的右支上
        if node.left != None:
            node.left.parent = node

        temp.right = node
        node.parent = temp

        # temp took over node's place so now its parent should point to temp
        if temp.parent != None:
            if node == temp.parent.left:
                temp.parent.left = temp
            else:
                temp.parent.right = temp
        else:
            self.root = temp

        return temp

if __name__ == "__main__":
    # 未测试
    pass