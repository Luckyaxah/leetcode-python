class Solution:
    def hammingWeight1(self, n: int) -> int:
        count = 0
        while n:
            if n & 1 == 1:
                count += 1
            n = n >> 1
        return count
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += 1
            n = n & (n-1)
        return count

if __name__ == "__main__":
    a = Solution()
    print(a.hammingWeight(0b110110))