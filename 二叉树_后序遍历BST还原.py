class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def buildTree(arr, L, R):
    if L > R:
        return None
    head = TreeNode(arr[R])
    if L == R:
        return head
    # arr[L..R-1] < arr[R] L, M
    #             > arr[R] M+1, R-1
    M = R-1
    for i in range(L, R):
        if arr[i]>arr[R]:
            M = i-1
            break
    head.left = buildTree(arr, L, M)
    head.right = buildTree(arr, M+1, R-1)
    return head
    
    

from 二叉树_打印二叉树 import printTree

arr = [1,3,2,6,8,7,5]
N = len(arr)
printTree(buildTree(arr, 0, N-1))