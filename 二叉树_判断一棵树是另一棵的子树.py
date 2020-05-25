from 二叉树_序列化与反序列化 import deserializeByPre
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def serializeByPre(root):
            if not root:
                return "#_"
            res = str(root.val) + "_"
            res+= serializeByPre(root.left)
            res+= serializeByPre(root.right)
            return res
        str_s = '_'+serializeByPre(s)
        str_t = '_'+serializeByPre(t)
        ret = str_t in str_s
        return ret

if __name__ == "__main__":
    a = "12_#_#_"
    b = "2_#_#_"
    c = Solution()
    print(c.isSubtree(deserializeByPre(a),deserializeByPre(b)))

