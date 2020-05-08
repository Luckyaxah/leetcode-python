class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if not strs or not strs[0]:
            return ''
        if len(strs) == 1:
            return strs[0]
        common_prefix = strs[0]
        for i in range(1,len(strs)):
            if not strs[i]:
                return ''
            j = 0
            com_len = len(common_prefix)
            new_str_len = len(strs[i])
            while True:
                if com_len == j:
                    break
                if new_str_len == j:
                    common_prefix = strs[i]
                    break
                if common_prefix[j] != strs[i][j]:
                    common_prefix = common_prefix[:j]
                    break
                j += 1
        return common_prefix         


if __name__ == "__main__":
    a = Solution()
    print(a.longestCommonPrefix(['flower','flow','flight']))
    # print(a.longestCommonPrefix([""]))