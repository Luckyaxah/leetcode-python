
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def process(root):
            if not root:
                return 0
            max_height = 0
            if root.children:
                for node in root.children:
                    max_height = max(max_height, process(node))
            return max_height + 1
        if not root:
            return 0
        return process(root)

if __name__ == "__main__":
    head = Node(1, [])
    head.children.append(Node(3, []))
    head.children.append(Node(2))
    head.children.append(Node(4))
    head.children[0].children.append(Node(5))
    head.children[0].children.append(Node(6))
    print(Solution().maxDepth(head))