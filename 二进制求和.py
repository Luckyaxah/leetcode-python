class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c = str(int(a)+int(b))
        c = list(map(int,c))
        len_c = len(c)
        carry = 0
        for i in range(len_c-1,-1,-1):
            if c[i]+carry >1:
                c[i] = c[i]+carry -2
                carry = 1
            else:
                c[i] = c[i]+carry
                carry = 0
        if carry == 1:
            c.insert(0,1)
        ret =''
        for i in range(len(c)):
            ret += str(c[i])
        return ret
if __name__ == "__main__":
    a = Solution()
    print(a.addBinary('1010','1011'))