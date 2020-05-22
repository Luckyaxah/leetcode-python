# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from 链表类 import ListNode
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        p1 = head
        length = 0
        while p1:
            target = p1
            for j in range(length-1, -1, -1):
                p2 = head
                t = 0
                while t<j:
                    p2 = p2.next
                    t += 1
                if p2.val>target.val:
                    temp = p2.val
                    p2.val = target.val
                    target.val = temp
                    target = p2
                else:
                    break
            p1 = p1.next
            length+= 1
        return head

    def insertionSortList1(self, head: ListNode) -> ListNode:
        if not head:
            return head
        cur, nxt = head, head.next
        dummy = ListNode(float('-inf'))
        dummy.next = head
        while nxt:
            if nxt.val >= cur.val:
                cur, nxt = nxt, nxt.next
            else:
                cur.next = nxt.next
                pre1, pre2 = dummy, dummy.next
                while nxt.val > pre2.val:
                    pre1, pre2 = pre2, pre2.next
                pre1.next = nxt
                nxt.next = pre2
                nxt = cur.next
        return dummy.next

if __name__ == "__main__":
    a = Solution()
    l = ListNode([4,2,1,3])
    print(l)
    print(a.insertionSortList(l))
