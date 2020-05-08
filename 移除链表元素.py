from 链表类 import ListNode
class Solution:
    def removeElements1(self, head: ListNode, val: int) :
        """
        删除链表中等于给定值val的所有节点
        """
        if not head:
            return []
        while head:
            if head.val == val:
                if head.next:
                    head.val = head.next.val
                    head.next = head.next.next
                else:
                    return []
            else:
                break
        if not head:
            return []
        root = head

        pre = root
        head = pre.next
        while head:
            if head.val == val:
                if head.next:
                    pre.next = head.next
                    head = head.next
                else:
                    pre.next = None
                    head = None
            else:
                pre = head
                head = head.next
        return root

    def removeElements(self, head: ListNode, val: int) :
        """
        删除链表中等于给定值val的所有节点
        """
        root = head
        while root:
            if root.val != val:
                break
            else:
                root = root.next
        if not root:
            return []
        pre = root
        cur = root.next
        while cur:
            if cur.val == val:
                pre.next = cur.next
                cur = pre.next
            else:
                pre = cur
                cur = cur.next
        return root

if __name__ == "__main__":
    a = Solution()
    l = ListNode([2,1,2,3,4,2])
    root = a.removeElements(l,2)
    root._print()