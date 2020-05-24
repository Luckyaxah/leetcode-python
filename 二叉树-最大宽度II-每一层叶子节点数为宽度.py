class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""
这里认为每一层叶子节点数为宽度
"""
def process(head):
    if not head:
        return
    from queue import Queue
    q = Queue()
    level_map ={}
    q.put(head)
    level_map[head] = 1
    c_level = 1
    c_nodes = 0
    max_c_nodes = 0
    while not q.empty():
        cur = q.get()
        level = level_map.get(cur)
        if level == c_level:
            c_nodes +=1
        else:
            print("level " +str(c_level) + ", nodes "+ str(c_nodes))
            max_c_nodes = c_nodes if c_nodes> max_c_nodes else max_c_nodes
            c_nodes = 1
            c_level += 1
        print("node:" + str(cur.val) + ", Level: "+ str(level) )
        if cur.left:
            level_map[cur.left] = level+1
            q.put(cur.left)
        if cur.right:
            level_map[cur.right] = level+1
            q.put(cur.right)
        # print(q)
    print("level " +str(c_level) + ", nodes "+ str(c_nodes))
    max_c_nodes = c_nodes if c_nodes> max_c_nodes else max_c_nodes
    return max_c_nodes


if __name__ == "__main__":
    head = TreeNode(1)
    head.left = TreeNode(2)
    head.right = TreeNode(3)
    head.left.left = TreeNode(4)
    head.left.right = TreeNode(5)
    head.right.left = TreeNode(6)
    head.right.right = TreeNode(7)
    head.left.right.right = TreeNode(8)
    head.right.left.left = TreeNode(9)
    head.right.right.right = TreeNode(10)

    print("max:", process(head))