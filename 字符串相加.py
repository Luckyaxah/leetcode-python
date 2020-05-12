class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        l1 = len(num1)
        l2 = len(num2)
        if l2>l1:
            num2, num1 = num1, num2
            l2, l1 = l1, l2
        # num1 = list(reversed(num1))
        # num2 = list(reversed(num2))
        p = 0
        ret = ''
        for i in range(0,l1):
            j = l1-1-i
            if j>l1-l2-1:
                n = int(num1[j]) + int(num2[j-(l1-l2)]) + p
            else:
                n = int(num1[j]) + p
            if n > 9:
                p = 1
                n = n-10
            else:
                p = 0
            ret = str(n)+ret
        if p>0:
            ret = str(p)+ret
        return ret
                
if __name__ == "__main__":
    a = Solution()
    n1 = '1251'
    n2 = '245'
    print(a.addStrings(n1,n2))