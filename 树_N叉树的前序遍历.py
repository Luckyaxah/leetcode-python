"""
# Definition for a Node.

"""
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node'):
        ret = []
        def process(root):
            if not root:
                return
            ret.append(root.val)
            if root.children:
                for node in root.children:
                    process(node)
        process(root)
        return ret

if __name__ == "__main__":
    head = Node(1, [])
    head.children.append(Node(3, []))
    head.children.append(Node(2))
    head.children.append(Node(4))
    head.children[0].children.append(Node(5))
    head.children[0].children.append(Node(6))
    print(Solution().preorder(head))