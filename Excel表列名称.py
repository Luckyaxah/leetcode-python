class Solution:
    def convertToTitle(self, n: int) -> str:
        col = ''
        devide = 26
        while n:
            n = n-1
            temp = n % devide
            col = chr(ord('A')+temp) + col
            n = n // devide
        return col

if __name__ == "__main__":
    a = Solution()
    print(a.convertToTitle(3))
    print(a.convertToTitle(28))
    print(a.convertToTitle(701))