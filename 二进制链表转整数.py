from 链表类 import ListNode
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        ret = 0
        if not head:
            return []
        while head:
            if head.val == 0:
                head = head.next
            else:
                break
        while head:
            ret = ret << 1
            ret += head.val
            head = head.next
        return ret
if __name__ == "__main__":
    a = Solution()
    l = ListNode([1,0,1])
    print(a.getDecimalValue(l))