class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for char in s:
            if not char in d:
                d[char] = 1
            else:
                d[char] += 1
        for ind, char in enumerate(s):
            if d[char] == 1:
                return ind
        return -1

if __name__ == "__main__":
    a = Solution()
    print(a.firstUniqChar('leetcode'))
    print(a.firstUniqChar('loveleetcode'))