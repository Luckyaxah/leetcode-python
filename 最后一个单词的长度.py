class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        len_s = len(s)
        start = len_s-1

        while not ( (s[start] >= 'A' and s[start] <='Z') or (s[start] >= 'a' and s[start] <='z') ):
            start -= 1
            if start <0:
                return 0
        for i in range(start,-1,-1):
            if s[i] == ' ':
                return start -i
        return start+1

if __name__ == "__main__":
    a = Solution()
    # print(a.lengthOfLastWord('Hello World'))
    print(a.lengthOfLastWord(' '))