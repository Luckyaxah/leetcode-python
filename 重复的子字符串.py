class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        def helper(s, p):
            if len(s) % p != 0:
                return False
            j = 0
            for i in range(len(s)):
                if s[i] != s[j]:
                    return False
                else:
                    j = (j+1) % p
            return True
        for i in range(1, len(s)):
            if helper(s, i):
                return True
        return False
            

if __name__ == "__main__":
    print(Solution().repeatedSubstringPattern("abcdabcd"))