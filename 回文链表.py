from 链表类 import ListNode
from 反转链表 import Solution as S

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head :
            return True
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # 出循环时fast是最后一个节点，slow是中间节点或前半段的最后一个节点
        fast = S().reverseList(slow)
        slow = head
        # print("slow",slow)
        # print("fast",fast)
        while fast:
            if slow.val != fast.val:
                return False
            slow,fast = slow.next, fast.next
        return True
        
if __name__ == "__main__":
    a = Solution()
    t = ListNode.list2ListNode([1,2,3,3,2,1])
    print(t)
    print(a.isPalindrome(t))