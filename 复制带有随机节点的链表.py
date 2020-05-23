"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList1(self, head: 'Node') -> 'Node':
        d  = {}
        cur = head
        while cur:
            d[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            cur1 = d.get(cur)
            if cur.next:
                cur1.next = d.get(cur.next)
            if cur.random:
                cur1.random = d.get(cur.random)
            cur = cur.next
        return d.get(head)

    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return
        cur = head
        while cur:
            next_node = cur.next
            cur.next = Node(cur.val)
            cur.next.next = next_node
            cur = cur.next.next
        cur = head
        while cur:
            cur1 = cur.next
            if cur.random:
                cur1.random = cur.random.next
            cur = cur.next.next
        
        head1 = head.next
        cur = head
        while cur:
            cur1 = cur.next # cur1为cur对于的拷贝节点
            cur.next = cur1.next # 拷贝节点的下一个节点为原节点的下一个节点，这里还原原链表
            if not cur1.next:
                break
            cur1.next = cur1.next.next # 链接拷贝节点
            cur = cur.next 
        return head1
        

if __name__ == "__main__":
    a = Solution()
    l = Node(7)
    h = l

    for i in [13,11,10,1]:
        l.next = Node(i)
        l = l.next
    
    l = h
    l = l.next
    l.random = h


    head1 = a.copyRandomList(h)
    print(1)

    
