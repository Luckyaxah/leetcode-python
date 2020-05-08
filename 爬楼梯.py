class Solution:
    # def climbStairs1(self, n: int) -> int:
    #     if n== 1:
    #         return 1
    #     elif n == 2:
    #         return 2
    #     elif n == 3:
    #         return 3
    #     last_ret = self.climbStairs(n-2)+self.climbStairs(n-1)
    #     return last_ret
    def climbStairs(self, n: int) -> int:
        pre1 = 0
        pre2 = 1
        for i in range(n):
            temp =pre2
            pre2 =pre1+pre2
            pre1 = temp
        return pre2
if __name__ == "__main__":
    a = Solution()
    print(a.climbStairs(4))