# Definition for a binary tree node.
# 可以使用中序遍历进行解决
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Info:
    def __init__(self, _max, _min, df):
        self._max = _max
        self._min = _min
        self.df = df
import math

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        def process(root):
            if not root:
                return None
            linfo = process(root.left)
            rinfo = process(root.right)
            if not linfo and not rinfo:
                return Info(root.val, root.val, math.inf)
            if linfo and not rinfo:
                df = min(root.val - linfo._max, linfo.df)
                _max = root.val
                _min = linfo._min
                return Info(_max, _min, df)
            if rinfo and not linfo:
                df = min(rinfo._min - root.val, rinfo.df)
                _min = root.val
                _max = rinfo._max
                return Info(_max, _min, df)
            # rinfo和linfo都存在
            df = min(root.val - linfo._max, linfo.df,  rinfo._min - root.val, rinfo.df)
            _min = linfo._min
            _max = rinfo._max
            return Info(_max, _min, df)
        ret = process(root)
        return ret.df
                