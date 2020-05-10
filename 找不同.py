class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d = {}
        for i in s:
            if not i in d:
                d[i] = 1
            else:
                d[i] += 1
        for i in t:
            if not i in d:
                return i
            else:
                d[i] -= 1
        for k in d:
            if d[k] < 0:
                return k

if __name__ == "__main__":
    a = Solution()
    print(a.findTheDifference('abcd','abcde'))