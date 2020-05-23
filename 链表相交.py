# Definition for singly-linked list.
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
def noLoop(headA, headB):
    if (not headA) or (not headB):
        return
    cur1 = headA
    cur2 = headB
    n = 0
    while cur1.next:
        n += 1
        cur1 = cur1.next
    while cur2.next:
        n -= 1
        cur2 = cur2.next
    if cur1 != cur2:
        return

    cur1 = headA if n>0 else headB
    cur2 = headB if cur1 == headA else headA
    n = abs(n)
    while n:
        cur1 = cur1.next
        n -= 1
    while cur1 != cur2:
        cur1 = cur1.next
        cur2 = cur2.next
    return cur1

def bothLoop(headA,loopA,headB,loopB):
    if loopA == loopB:
        cur1 = headA
        cur2 = headB
        n = 0
        while(cur1 != loopA):
            n += 1
            cur1 = cur1.next
        while cur2 != loopB:
            n -= 1
            cur2 = cur2.next
        cur1 = headA if n>0 else headB
        cur2 = headB if cur1 == headA else headA
        n = abs(n)
        while n:
            cur1 = cur1.next
            n -= 1
        while cur1 != cur2:
            cur1 = cur1.next
            cur2 = cur2.next
        return cur1
    else:
        cur1 = loopA.next
        while cur1 != loopA:
            if cur1 == loopB:
                return loopA
            cur1 = cur1.next
        return None

    
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if (not headA) or (not headB):
            return
        loopA = getLoopNode(headA)
        loopB = getLoopNode(headB)
        if (not loopA) and (not loopB):
            return noLoop(headA, headB)
        if loopA and loopB:
            return bothLoop(headA, loopA, headB, loopB)
        return None
        

if __name__ == "__main__":
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    a.next.next.next = ListNode(4)

    b = ListNode(5)
    b.next = a.next.next.next
