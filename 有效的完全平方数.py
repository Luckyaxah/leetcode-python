class Solution:
    def isPerfectSquare1(self, num: int) -> bool:
        i = 1
        if num == 1:
            return True
        while i <= num // 2:
            temp =i **2
            if temp == num:
                return True
            elif temp >num:
                return False
            i+= 1
        return False
    def isPerfectSquare2(self, num: int) -> bool:
        start = 1
        end = num
        temp1 = -1
        n = 0
        while temp1 != n:
            temp1 = n
            n = (start + end) // 2
            temp = n**2
            if temp == num:
                return True
            elif temp < num:
                start = n
            else:
                end = n
        return False

    def isPerfectSquare(self, num: int) -> bool:
        start = 1
        end = num
        while start<= end:
            n = (start + end) // 2
            temp = n**2
            if temp == num:
                return True
            elif temp < num:
                start = n+1
            else:
                end = n-1
        return False



if __name__ == "__main__":
    a = Solution()
    print(a.isPerfectSquare(16))