from 二叉树_打印二叉树 import printTree
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def serializeByPre(root):
    if not root:
        return "#_"
    res = str(root.val) + "_"
    res+= serializeByPre(root.left)
    res+= serializeByPre(root.right)
    return res
def deserializeByPre(preStr):
    values = preStr.split('_')
    from queue import Queue
    q = Queue()
    for i in values:
        q.put(i)
    return reconPreOrder(q)

def reconPreOrder(q):
    value = q.get()
    if value=='#':
        return None
    head = TreeNode(int(value))
    head.left = reconPreOrder(q)
    head.right = reconPreOrder(q)
    return head


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        return serializeByPre(root)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        return deserializeByPre(data)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

if __name__ == "__main__":
    a = "1_1_#_1_#_#_#_"
    codec = Codec()
    head = codec.deserialize(a)
    printTree(head)
    print(codec.serialize(head))
