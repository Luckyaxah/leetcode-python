class Solution:
    def mySqrt(self, x):
        i = 1
        while True: 
            if x/i == i:
                return i
            elif x/ i < i:
                return i-1
            i += 1
if __name__ == "__main__":
    a = Solution()
    print(a.mySqrt(10))