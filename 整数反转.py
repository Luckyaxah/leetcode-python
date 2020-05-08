class Solution:
    
    def reverse1(self, x: int) -> int:
        if -10<x and x<10:
            return x
        self.p = 1
        def fun(x):
            a1 = x // 10
            a2 = x % 10
            if a1 < 10:
                self.p = self.p*10
                return a2*self.p+a1
            t = self.reverse(a1)
            self.p = self.p*10
            return a2*self.p + t
        if x<0:
            temp = fun(-x)
            return -temp if -temp >= -2**31 else 0
        temp = fun(x) 
        return temp if temp <= 2**31-1 else 0 

    def reverse(self, x: int) -> int:
        Flag = False
        if x<0:
            Flag = True
            x = -x
        p = []
        while x:
            p.append(x % 10)
            x = x // 10
        factor = 1
        ret = 0
        while p:
            ret =ret+ factor *p.pop()
            factor *= 10

        if Flag:
            if ret > 2**31-1:
                return 0
            return -ret
        if ret > 2**31:
            return 0
        return ret

if __name__ == "__main__":
    a = Solution()
    print(a.reverse(-1235))