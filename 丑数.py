class Solution:
    def isUgly(self, num: int) -> bool:
        """
        丑数就是只包含质因数 2, 3, 5 的正整数。
        """
        if num<=0:
            return False
        for i in [2,3,5]:
            while True:
                if num % i == 0:
                    # print(num)
                    num = num // i
                else:
                    break
        if num == 1:
            return True
        return False

if __name__ == "__main__":
    a = Solution()
    # print(a.isUgly(1))
    # print(a.isUgly(6))
    # print(a.isUgly(8))
    print(a.isUgly(-2147483648))