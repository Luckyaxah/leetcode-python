class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def getLoopNode( head: ListNode) -> ListNode:
    if (not head ) or (not head.next) or (not head.next.next):
        return None
    s = head.next
    f = head.next.next
    while s != f:
        if (not f) or (not f.next):
            return None
        s = s.next
        f = f.next.next
    f = head
    while f != s:
        f = f.next
        s = s.next
    return f

if __name__ == "__main__":
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    a.next.next.next = ListNode(4)
    a.next.next.next.next = ListNode(5)
    a.next.next.next.next.next = ListNode(6)
    a.next.next.next.next.next.next = a.next.next.next

    intersection = getLoopNode(a)
    print(intersection.val)
    # b = ListNode(5)
    # b.next = a.next.next.next