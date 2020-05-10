class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        d = {}
        for i in magazine:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for i in ransomNote:
            if not i in d:
                return False
            else:
                d[i] -= 1
                if d[i] < 0:
                    return False
        return True

if __name__ == "__main__":
    a = Solution()
    print(a.canConstruct('aa','aab'))
    print(a.canConstruct('aa','ab'))