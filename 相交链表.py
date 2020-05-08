from 链表类 import ListNode

class Solution:
    def getIntersectionNode1(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return
        node_a = headA
        node_b = headB
        len_a = 1
        while node_a.next:
            len_a += 1
            node_a = node_a.next
        len_b = 1
        while node_b.next:
            len_b += 1
            node_b = node_b.next
        node_a = headA
        node_b = headB
        while len_a >len_b:
            node_a = node_a.next
            len_a -= 1
        while len_b >len_a:
            node_b = node_b.next
            len_b -= 1
        while node_a:
            if node_a is node_b:
                return node_a
            else:
                node_a = node_a.next
                node_b = node_b.next
        return

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        ha, hb = headA, headB
        while ha != hb:
            ha = ha.next if ha else headB
            hb = hb.next if hb else headA
        return ha

        
        
        

if __name__ == "__main__":
    a = Solution()
