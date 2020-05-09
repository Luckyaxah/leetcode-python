class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        while n :
            if n % 4 == 0:
                n = n // 4
            else:
                break
        return n == 1
    
if __name__ == "__main__":
    a = Solution()
    print(a.isPowerOfFour(16))