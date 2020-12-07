class Solution:
    # def judgeSquareSum(self, c: int) -> bool:
    #     n = c+1
    #     l = []
    #     for i in range(n):
    #         if int(i ** 0.5) ** 2 == i:
    #             l.append(i)
    #     d = []
    #     for i in l:
    #         if i+i == c:
    #             return True
    #         if i in d:
    #             return True
    #         d.append(c-i)
    #     return False
    def judgeSquareSum1(self, c: int) -> bool:
        a = 0
        while a * a <= c:
            b = c - a * a
            b = b ** 0.5
            if b == int(b):
                return True
            a += 1
        return False


if __name__ == "__main__":
    n = 4
    print(Solution().judgeSquareSum1(n))