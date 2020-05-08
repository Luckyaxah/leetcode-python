from 链表类 import ListNode

class Solution:
    def deleteDuplicates(self, head):   # 不返回结果
        if not head:
            return
        while head.next and head.val == head.next.val:
            head.next = head.next.next
        self.deleteDuplicates(head.next)
        return
    
    def deleteDuplicates1(self, head):  # 要返回结果
        def fun(head):
            if not head:
                return
            while head.next and head.val == head.next.val:
                head.next = head.next.next
            fun(head.next)
        fun(head)
        return head
if __name__ == "__main__":
    a = Solution()
    obj =  ListNode.list2ListNode([1,2,3,3]) 
    a.deleteDuplicates(obj)
    obj._print()