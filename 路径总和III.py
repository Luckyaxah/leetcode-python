from 二叉树类 import TreeNode

class Solution:
    def pathSum1(self, root, sum: int) -> int:
        def helper(root, rets):
            if not root:
                return []
            ret = [[root.val]]
            l = helper(root.left,rets)
            if l:
                ret+= [[root.val]+ item for item in l]
            r = helper(root.right,rets)
            if r:
                ret+= [[root.val]+ item for item in r]
            rets += ret
            return ret
        def get_sum(l):
            ret = 0
            for i in l:
                ret += i
            return ret

        rets = []
        helper(root, rets)

        count = 0 
        for i in rets:
            if get_sum(i) == sum:
                count += 1

        return count

    def pathSum2(self, root, sum: int) -> int:
        count = [0]
        def helper(root,count):
            # 返回以root为起点的所有子路径
            if not root:
                return []
            ret = [root.val]
            l = helper(root.left,count)
            if l:
                ret+= [root.val+ item for item in l]
            r = helper(root.right,count)
            if r:
                ret+= [root.val+ item for item in r]
            for i in ret:
                if i == sum:
                    count[0] += 1
            return ret
        helper(root,count)
        return count[0]

    def pathSum(self, root, sum: int) -> int:
        def helper(root):
            # 返回以root为起点的所有子路径的和
            if not root:
                return [],0
            ret = [root.val]
            l,lcount = helper(root.left)
            if l:
                ret+= [root.val+ item for item in l]
            r,rcount = helper(root.right)
            if r:
                ret+= [root.val+ item for item in r]
            count = 0
            for i in ret:
                if i == sum:
                    count += 1

            return ret, count+lcount+rcount
        temp, count = helper(root)
        return count

    def pathSum3(self, root, sum: int) -> int:
        def helper(root):
            # 返回以root为起点的所有子路径的和
            if not root:
                return [],0
            count = 0
            if root.val == sum:
                count += 1
            ret = [root.val]
            l,lcount = helper(root.left)
            if l:
                for item in l:
                    if root.val + item == sum:
                        count += 1
                    ret.append(root.val+item)
                # ret+= [root.val+ item for item in l]
            r,rcount = helper(root.right)
            if r:
                # ret+= [root.val+ item for item in r]
                for item in r:
                    if root.val + item == sum:
                        count += 1
                    ret.append(root.val+item)
            return ret, count+lcount+rcount
        temp, count = helper(root)
        return count

if __name__ == "__main__":
    a = Solution()
    t = TreeNode([10,5,-3,3,2,None,11])
    print(a.pathSum(t,8))
