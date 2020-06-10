# 空间复杂度可达到O(1)，而常规遍历的空间复杂度是O(h)

def morrisIsBst(head):
    if head == None:
        return
    cur = head
    mostRight = None
    pre = None
    while cur != None:
        mostRight = cur.left
        if mostRight != None: # 可以来到自己两次的节点
            while mostRight.right != None and mostRight.right != cur:
                mostRight = mostRight.right
            if mostRight.right == None: 
                mostRight.right = cur
                cur = cur.left
                continue
            else:
                print(cur.val)
                if pre != None and cur.val <= pre:
                    return False
                pre = cur.val
                mostRight.right = None
        else:
            # 只能来到自己一次的节点
            print(cur.val)
            if pre != None and cur.val <= pre:
                return False
            pre = cur.val
        cur = cur.right
    return True

if __name__ == "__main__":
    from 二叉树_打印二叉树 import printTree
    from 二叉树_序列化与反序列化 import Codec
    t_s = '5_2_1_#_#_3_#_#_8_7_#_#_10_#_#_'
    t = Codec().deserialize(t_s)
    printTree(t)

    print(morrisIsBst(t))

    t_s1 = '5_3_1_#_#_2_#_#_8_7_#_#_10_#_#_'
    t1 = Codec().deserialize(t_s1)
    print(morrisIsBst(t1))

