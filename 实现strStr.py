class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_haystack = len(haystack)
        len_needle = len(needle)
        if len_needle ==0:
            return 0
        if len_haystack == 0 or len_haystack < len_needle:
            return -1
        max_ind = len_haystack-len_needle+1
        i = 0
        while i < max_ind:
            Flag = True
            for j in range(len_needle):
                if haystack[i+j] != needle[j]:
                    i += 1
                    Flag = False
                    break
            if Flag:
                return i
        return -1

if __name__ == "__main__":
    a = Solution()
    print(a.strStr('hello','ll'))