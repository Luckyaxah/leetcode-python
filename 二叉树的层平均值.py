# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def averageOfLevels(self, root):
        def helper(root,k):
            if not root:
                return
            if k<len(totals):
                totals[k] += root.val
                counts[k] += 1
            else:
                totals.append(root.val)
                counts.append(1)
            helper(root.left, k+1)
            helper(root.right, k+1)
        
        counts = list()
        totals = list()
        helper(root, 0)
        return [total/count for total, count in zip(totals, counts)]
        