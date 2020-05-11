class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        for i in s:
            if not i in d:
                d[i] = 1
            else:
                d[i] += 1
        ret = 0
        m = 0
        for i in d:
            if d[i] % 2 ==0:
                ret += d[i]
            else:
                ret += d[i]-1
        if ret < len(s):
            ret += 1
        return ret

if __name__ == "__main__":
    a = Solution()
    print(a.longestPalindrome("civilwartestingwhee"))