class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'I':1,'V':5,'X':10,'L':50,
        'C':100,'D':500,'M':1000,'IV':4,'IX':9,
        'XL':40,'XC':90,'CD':400,'CM':900}
        s_list = list(s)
        ret = 0
        while s_list:
            char = s_list.pop(0)
            if char == 'I' and s_list and ( s_list[0]=='V' or s_list[0]=='X' ):
                char += s_list.pop(0)
            if char == 'X' and s_list and ( s_list[0]=='L' or s_list[0]=='C' ):
                char += s_list.pop(0)
            if char == 'C' and s_list and ( s_list[0]=='D' or s_list[0]=='M' ):
                char += s_list.pop(0)
            ret += dic[char]
        return ret

if __name__ == "__main__":
    a = Solution()
    print(a.romanToInt('MCMXCIV'))