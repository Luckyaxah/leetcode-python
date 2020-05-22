from 链表类 import ListNode
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:

        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

if __name__ == "__main__":
    a = Solution()
    l = ListNode([1,2,3,4,5])
    print(a.middleNode(l))