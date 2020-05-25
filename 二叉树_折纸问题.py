# 给定一个二叉树，返回它的中序遍历。
# 规则：若树为空，则空操作返回，否则从根节点开始（注意不是先访问根节点）中序遍历根节点的左子树，最后访问根节点
# 最后中序遍历右子树
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def printAllFolds(N):
    printProcess(1,N,True)
# down == True 凹， down == False 凸
def printProcess(i, N, down):
    if i>N:
        return
    printProcess(i+1, N, True)
    print('凹' if down==True else '凸')
    printProcess(i+1, N, False)

if __name__ == "__main__":
    N = 3
    printAllFolds(N)