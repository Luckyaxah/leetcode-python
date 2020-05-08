class Solution:
    def trailingZeroes(self, n: int) -> int:
        result=0
        n_fake=n
        while n_fake>=5:
            n_fake//=5
            result+=n_fake
        return result

if __name__ == "__main__":
    a = Solution()
    print(a.trailingZeroes(3))
    print(a.trailingZeroes(5))
    print(a.trailingZeroes(10))
    print(a.trailingZeroes(25))
    print(a.trailingZeroes(30))