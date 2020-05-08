class Solution:
    def canWinNim(self, n: int) -> bool:
        if n % 4 == 0:
            return False
        return True

if __name__ == "__main__":
    a = Solution()
    print(a.canWinNim(4))