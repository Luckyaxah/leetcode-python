class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        elif n == 2:
            return '11'
        elif n == 3:
            return '21'
        elif n == 4:
            return '1211'
        elif n == 5:
            return '111221'
        ret = self.countAndSay(n-1)
        if n== 4:
            print(1)
        n_str = ''
        i = 0
        count = 0
        num = ret[0]
        len_ret = len(ret)
        while i < len_ret:
            if ret[i] != num:
                n_str += '%d%s'%(count,num)
                count = 1
                num = ret[i]
            else:
                count += 1
            i += 1
        n_str += '%d%s'%(count,num)
        return n_str

if __name__ == "__main__":
    a = Solution()
    print(a.countAndSay(6))