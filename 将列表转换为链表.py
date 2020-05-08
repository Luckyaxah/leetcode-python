from 链表类 import ListNode

# def list2ListNode(l):
#     if not l:
#         return None # 最后返回None
#     ret = ListNode(l.pop(0))
#     ret.next = list2ListNode(l)
#     return ret

if __name__ == "__main__":
    l = [1,3,4]
    # l1 = ListNode(1)
    # l1.next = ListNode(3)
    # l1.next.next = ListNode(4)
    # l1._print()
    ListNode.list2ListNode(l)._print()