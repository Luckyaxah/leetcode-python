class Solution:
    def arrangeCoins1(self, n: int) -> int:
        i = 1
        count = 0
        while n>=0:
            n -= i
            count += 1
            i += 1
        if n<0:
            count -= 1
        return count

    def arrangeCoins(self, n: int) -> int:
        # i = 1
        count = 0
        while n>=0:
            n -= count
            count += 1
            # i += 1
        count -= 1
        if n<0:
            count -= 1
        return count


if __name__ == "__main__":
    a = Solution()
    print(a.arrangeCoins(8))