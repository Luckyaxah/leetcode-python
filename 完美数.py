class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num < 1:
            return False
        factor = 1
        for i in range(2,int(num**0.5)+1):
            if num % i == 0:
                if i != num ** 0.5:
                    factor += i
                    factor += num / i
                else:
                    factor += i
        if factor == num:
            return True
        return False

print(Solution().checkPerfectNumber(6))
# print(Solution().checkPerfectNumber(28))