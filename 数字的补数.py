class Solution:
    def findComplement(self, num: int) -> int:
        if num< -2**31 or num> 2**31-1:
            raise RuntimeError("Wrong")
        count = 0
        temp = num
        if temp > 0:
            while temp:
                temp = temp >> 1
                count += 1
        print(bin(2**count-1-num))
        return 2**count-1-num

if __name__ == "__main__":
    print(Solution().findComplement(5))
    print(Solution().findComplement(1))