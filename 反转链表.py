from 链表类 import ListNode
class Solution:
    def reverseList1(self, head: ListNode) -> ListNode:
        if not head:
            return []
        l = []
        while head:
            l.append(head)
            head=head.next
        root = l.pop()
        head = root
        while l:
            head.next = l.pop()
            head = head.next
        head.next = None
        return root

    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return []
        pre = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre
        

if __name__ == "__main__":
    a = Solution()
    l = ListNode([1,2,3,4,5])
    # q = a.reverseList(l)
    print(l)
    # print(q)
