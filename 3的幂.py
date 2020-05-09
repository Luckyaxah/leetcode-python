class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n :
            if n % 3 == 0:
                n = n // 3
            else:
                break
        return n == 1

    def isPowerOfThree1(self, n: int) -> bool:
        return n>0 and 1162261467 % n == 0


if __name__ == "__main__":
    a = Solution()
    print(a.isPowerOfThree(9))
    print(a.isPowerOfThree(45))