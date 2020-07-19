class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = S.replace('-', '').upper()
        s_len = len(S)
        first = s_len % K
        group = s_len // K + 1
        if first == 0:
            first = K
            group -= 1
        ret = ''
        p = 0
        q = first
        for _ in range(group):
            ret += S[p:q]
            ret += '-'
            p = q
            q = q + K
        ret = ret[:-1]
        return ret

if __name__ == "__main__":
    print(Solution().licenseKeyFormatting('5F3Z-2e-9-w', 4))
    print(Solution().licenseKeyFormatting('2-5g-3-J', 2))