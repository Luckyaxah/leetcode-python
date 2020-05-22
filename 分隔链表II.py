from 链表类 import ListNode

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        arr = []
        # pre = None
        cur = head
        # less = head
        while cur:
            arr.append(cur)
            # if cur.val < x:
            #     swap(cur)
            cur = cur.next
        less = -1
        more = len(arr)
        # for i in range(len(arr)):
        i = 0
        while i<more:
            if arr[i].val< x:
                arr[less+1], arr[i] = arr[i], arr[less+1]
                less += 1
                i += 1
            elif arr[i].val> x:
                arr[more-1], arr[i] = arr[i], arr[more-1]
                more -= 1
            elif arr[i].val == x:
                i+= 1
        for i in range(len(arr)-1):
            arr[i].next = arr[i+1]
        arr[len(arr)-1].next = None
        return arr[0]


        

if __name__ == "__main__":
    a = Solution()
    l = ListNode([1,4,3,2,5,2])
    print(a.partition(l, 3))