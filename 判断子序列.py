class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)
        if len_s > len_t:
            return False
        if not s:
            return True
        s_flag = 0
        t_flag = 0
        while t_flag < len_t:
            if s[s_flag] == t[t_flag]:
                s_flag += 1
            if s_flag == len_s:
                return True
            t_flag += 1
        return False


if __name__ == "__main__":
    a = Solution()
    s = 'abc'
    t = 'ahbgdc'
    print(a.isSubsequence(s,t))