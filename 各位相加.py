class Solution:
    def addDigits1(self, num: int) -> int:
        ret = num
        while ret>=10:
            temp = ret
            ret = 0
            while temp:
                ret += temp % 10
                temp = temp // 10
        return ret

    def addDigits(self, num: int) -> int:
        return (num-1) % 9 +1

if __name__ == "__main__":
    a = Solution()
    print(a.addDigits(38))