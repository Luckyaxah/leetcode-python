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
    # 注：这里传入的是先序字符串
    values = preStr.split('_')
    return deserializeFromListByPre(values)

def deserializeFromListByPre(nodeLists):
    # 注：这里传入的是层序遍历字符串
    from queue import Queue
    q = Queue()
    for value in nodeLists:
        q.put(value)
    return reconPreOrder(q)

def deserializeByLevel(levelStr):
    # 注：这里传入的是层序遍历字符串
    values = levelStr.split('_')
    return deserializeFromListByLevel(values)

def deserializeFromListByLevel(nodeLists):
    from queue import Queue
    q = Queue()
    if len(nodeLists) %2 == 0:
        nodeLists.append('#')
    for value in nodeLists:
        if value != '#':
            q.put(TreeNode(int(value)))
        else:
            q.put(None)
    return reconLevelOrder(q)
    

def reconPreOrder(q):
    value = q.get()
    if value=='#':
        return None
    head = TreeNode(int(value))
    head.left = reconPreOrder(q)
    head.right = reconPreOrder(q)
    return head


def reconLevelOrder(q):
    from queue import Queue
    q1 = Queue()
    root = q.get()
    q1.put(root)
    while not q.empty():
        node = q1.get()
        node.left = q.get()
        q1.put(node.left)
        node.right = q.get()
        q1.put(node.right)
    return root

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

    b = ['1','2','#','3','4','#','#','#','#']
    head1 = deserializeFromListByPre(b)
    printTree(head1)

    b2 = ['1','2','#','3']

    head2 = deserializeFromListByLevel(b2)
    printTree(head2)

    b3 = '1_2_#_3'
    head3 = deserializeByLevel(b3)
    printTree(head3)

