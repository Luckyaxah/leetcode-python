class Solution:
    def toHex(self, num: int) -> str:
        if num >= 0:
            if num == 0:
                return '0'
            d={
                10:'a',
                11:'b',
                12:'c',
                13:'d',
                14:'e',
                15:'f'
            }
            ret = ''
            while num:
                t = num % 16
                t1 = d.get(t)
                n = t1 if t1 else str(t)
                ret = n+ret
                num = num // 16
            return ret
        else:
            return self.toHex(2**32+num)
        

if __name__ == "__main__":
    a = Solution()
    print(a.toHex(26))
    print(a.toHex(17))
    print(a.toHex(-1))