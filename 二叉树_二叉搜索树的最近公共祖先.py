from 二叉树类 import TreeNode
class Solution:
    """
    注意这里二叉树是二叉搜索树，节点N所有左子树上的节点都小于N，节点N所有右子树上的节点都大于N
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent_val = root.val
        p_val = p.val
        q_val = q.val
        if p_val<parent_val and q_val<parent_val:
            return self.lowestCommonAncestor(root.left,p,q)
        elif p_val>parent_val and q_val >parent_val:
            return self.lowestCommonAncestor(root.right,p,q)
        else:
            return root
            

if __name__ == "__main__":
    a = Solution()
    root = TreeNode([6,2,8,0,4,7,9,None,None,3,5])
    p = root.left
    q = root.right
    ret = a.lowestCommonAncestor(root,p,q)
    # print(ret.val)