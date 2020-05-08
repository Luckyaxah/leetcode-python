from 链表类 import ListNode

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next or not head.next.next:
            return False
        p = head
        q = head
        while p.next and q.next and q.next.next:
            p = p.next
            q = q.next.next
            if q == p:
                return True
        return False

if __name__ == "__main__":
    a = Solution()