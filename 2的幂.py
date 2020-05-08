class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n & n-1 == 0
if __name__ == "__main__":
    a = Solution()
    print(a.isPowerOfTwo(3))