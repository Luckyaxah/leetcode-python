class Solution:
    def isPalindrome1(self, s: str) -> bool:
        if not s:
            return True
        
        i = 0
        j = len(s)-1
        t1 = ""
        t2 = ""
        while i < j:
            while i<len(s):
                if s[i]>='A' and s[i]<='Z':
                    t1 = (chr(ord(s[i])-ord('A')+ord('a')))
                    break
                elif s[i]>='a' and s[i]<='z':
                    t1 =s[i]
                    break
                elif s[i]>='0' and s[i]<='9':
                    t1 =s[i]
                    break
                i += 1
            while j>-1:
                if s[j]>='A' and s[j]<='Z':
                    t2 = (chr(ord(s[j])-ord('A')+ord('a')))
                    break
                elif s[j]>='a' and s[j]<='z':
                    t2 =s[j]
                    break
                elif s[j]>='0' and s[j]<='9':
                    t2 =s[j]
                    break
                j -= 1
            if t1 != t2:
                return False
            i += 1
            j -= 1
        return True
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        s = list(s)
        l = len(s)
        i = 0
        while i<l:
            if s[i]>='A' and s[i]<='Z':
                s[i] = (chr(ord(s[i])-ord('A')+ord('a')))
            elif (s[i]>='a' and s[i]<='z') or (s[i]>='0' and s[i]<='9'):
                i += 1
            else:
                s.pop(i)
                l -= 1
        if s == s[-1::-1]:
            return True
        return False

            

if __name__ == "__main__":
    a = Solution()
    print(a.isPalindrome('A man, a plan, a canal: Panama'))
    print(a.isPalindrome("race a car"))
    print(a.isPalindrome("0P"))