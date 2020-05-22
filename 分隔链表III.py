from 链表类 import ListNode

class Solution:

    def partition(self, head: ListNode, x: int) -> ListNode:
        """
        分成左中右
        """
        sh = None
        st = None
        bh = None
        bt = None
        eh = None
        et = None
        while head:
            next = head.next
            head.next = None
            if head.val < x:
                if not sh:
                    sh = head
                    st = head
                else:
                    st.next = head
                    st = head
            elif head.val == x:
                if not eh:
                    eh = head
                    et = head
                else:    
                    et.next = head
                    et = head
            else:
                if not bh:
                    bh = head
                    bt = head
                else:
                    bt.next = head
                    bt = head
            head = next

        if st:
            st.next = eh
            et = st if not et else et # 谁连大于区域的头谁变成et
        if et:
            et.next = bh
        return sh if sh else (eh if eh else bh) 
            


        

if __name__ == "__main__":
    a = Solution()
    l = ListNode.list2ListNode([1,4,3,2,5,2])
    print(a.partition(l, 3))