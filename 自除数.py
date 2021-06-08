class Solution:
    def selfDividingNumbers(self, left: int, right: int):
        def isTheNumber(n):
            t = n
            while n:
                q = n % 10
                if q==0 or t % q != 0:
                    return False
                n = n // 10
            return True

        ret = []
        for num in range(left, right+1):
            if isTheNumber(num):
                ret.append(num)
        return ret

print(Solution().selfDividingNumbers(1,22))
        



