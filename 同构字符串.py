class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        for i in range(len(s)):
            if s[i] not in d:
                if t[i] in d.values():
                    return False
                d[s[i]]=t[i]
            elif d[s[i]] != t[i]:
                return False
        return True

if __name__ == "__main__":
    a = Solution()
    print(a.isIsomorphic("egg","add"))
    print(a.isIsomorphic("foo","bar"))
    print(a.isIsomorphic("ab","aa"))
    print(a.isIsomorphic("ab","ca"))
