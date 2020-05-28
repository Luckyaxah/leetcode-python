from 二叉树类 import TreeNode

class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:
        if not nums:
            return None
        len_nums = len(nums)
        if len_nums == 1:
            return TreeNode(nums[0])
        center = len_nums // 2
        root = TreeNode(nums[center])
        root.left = self.sortedArrayToBST(nums[:center])
        root.right = self.sortedArrayToBST(nums[center+1:])
        return root

if __name__ == "__main__":
    a = Solution()
    bst = a.sortedArrayToBST([-10,-3,0,5,9])
    bst._print()
