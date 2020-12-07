class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。
        """
        def checkPalindrome(low, high):
            i, j = low, high
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
            
        low, high = 0, len(s)-1
        while low < high:
            if s[low] == s[high]:
                low += 1
                high -= 1
            else:
                return checkPalindrome(low + 1, high) or checkPalindrome(low, high -1)
        return True