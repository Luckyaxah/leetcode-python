from 链表类 import ListNode
def reverseListNode(head):
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
    l = ListNode([1,2,3,4,5])
    print(l)
    print(reverseListNode(l))

