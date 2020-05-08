from 将列表转换为链表 import list2ListNode
from 链表类 import ListNode

class Solution:
    def mergeTwoLists(self, l1, l2):  
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val> l2.val:
            l3 = l2
            l2 = l2.next
        else:
            l3 = l1
            l1 = l1.next
        l3.next = self.mergeTwoLists( l1,l2)
        return l3

if __name__ == "__main__":
    a = Solution()
    l1 = list2ListNode([1,2,4])
    l2 = list2ListNode([1,3,4])

    l1._print()
    l2._print()

    l3 = a.mergeTwoLists(l1,l2)
    l3._print()