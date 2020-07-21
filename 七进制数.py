class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        ret = ''
        flag = num < 0
        if flag:
            num = -num
        while num:
            temp = num % 7
            ret = str(temp) + ret
            num = num // 7
        if flag:
            ret = '-' + ret
        return ret

if __name__ == "__main__":
    print(Solution().convertToBase7(0))