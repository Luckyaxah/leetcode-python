# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        if type(x) == list:
            ln = ListNode.list2ListNode(x)       # 返回的是第一个节点
            self.val = ln.val
            self.next = ln.next
        else:
            self.val = x
            self.next = None
    def _print(self):
        if not self.val:
            return
        print(self.val)
        if  self.next:
            self.next._print()
    def __str__(self):
        ret = ''
        head = self
        while head:
            ret += str(head.val) + '->'
            head = head.next
        ret += 'None'
        return ret
    def peek(self,n):
        # 只能对没有环的链表使用
        if n == -1 :
            def fun(x):
                if not x.next:
                    return x
                return fun(x.next)
            return fun(self)
        if n==0:
            return self
        return self.next.peek(n-1)
                
    def connect(self,pos):
        pass
    
    @classmethod
    def list2ListNode(cls,l):
        def fun(l):
            if not l:
                return None # 最后返回None       
            ret = ListNode(l.pop(0))
            ret.next = ListNode.list2ListNode(l)
            return ret
        ret = fun(l)
        return ret

if __name__ == "__main__":
    a = [3,2,0,-4]
    ln = ListNode.list2ListNode(a)

    print(ln.peek(1).val)
