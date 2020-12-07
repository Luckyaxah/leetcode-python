class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ptr = 0
        n = len(s)
        counts = []
        while ptr < n:
            c = s[ptr]
            count = 0
            while (ptr<n and s[ptr] == c):
                ptr += 1
                count += 1
            counts.append(count)
        ans = 0
        for i in range(1, len(counts)):
            ans += min(counts[i], counts[i-1])
        return ans