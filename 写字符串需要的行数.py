class Solution:
    def numberOfLines(self, widths, s: str) :
        linelimit = 100
        line = 1
        used = linelimit
        for c in s:
            taken = widths[ord(c)-ord('a')]
            if used >= taken:
                used -= taken
            else:
                used = linelimit - taken
                line += 1
        return [line, linelimit-used]

print(Solution().numberOfLines([4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],"bbbcccdddaaa"))
