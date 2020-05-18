class Solution:
    def fib(self, N: int) -> int:
        if N==0:
            return 0
        elif N==1:
            return 1
        t = 1
        t1 = 1
        while N-2:
            t, t1 = t1, t+t1
            N-=1
        return t1

if __name__ == "__main__":
    a = Solution()
    print(a.fib(30))

