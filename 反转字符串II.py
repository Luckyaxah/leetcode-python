class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        """
        给定一个字符串 s 和一个整数 k，你需要对从字符串开头算起的每隔 2k 个字符的前 k 个字符进行反转。
        """
        s = list(s)
        start = 0
        end = len(s)
        while start<end:
            if end - start < k:
                s[start:end] = s[start:end][::-1]
                break
            # if end - start < 2*k and end-start > k:
            #     s[start:start+k] = s[start:start+k][::-1]
            #     break
            s[start:start+k] = s[start:start+k][::-1]
            start += 2*k
            # print(s[start:start+k])
        return ''.join(s)
        

        

if __name__ == "__main__":
    s = 'abcdefg'
    k = 2
    print(Solution().reverseStr(s, k))