class Solution:
    def titleToNumber(self, s: str) -> int:
        col_num = 0
        devide = 1
        for i in range(len(s)-1,-1,-1):
            col_num +=(ord(s[i])-ord('A')+1 ) * devide
            devide *= 26
        return col_num

if __name__ == "__main__":
    a = Solution()
    print(a.titleToNumber('C'))
    print(a.titleToNumber('AB'))
    print(a.titleToNumber('ZY'))