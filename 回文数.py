class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        if x>0 and x% 10 == 0:
            return False
        p = []
        temp = x
        while temp:
            p.append(temp % 10)
            temp = temp// 10
        ret = 0
        factor = 1
        while p:
            ret += factor * p.pop()
            factor *= 10
        if x == ret:
            return True
        return False


if __name__ == "__main__":
    a = Solution()
    print(a.isPalindrome(121))
    print(a.isPalindrome(-121))
    print(a.isPalindrome(10))
    print(a.isPalindrome(1213121))

