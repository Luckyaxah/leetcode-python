class Solution:
    def reverseVowels(self, s: str) -> str:
        l = []
        vowels = ['a','e','i','o','u']
        for char in s:
            if char.lower() in vowels:
                l.append(char)
        ret = ''
        for char in s:
            if char.lower() in vowels:
                ret += l.pop()
            else:
                ret += char
        return ret
        

        




if __name__ == "__main__":
    a = Solution()
    print(a.reverseVowels("leetcode"))