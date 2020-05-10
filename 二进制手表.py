class Solution:
    def readBinaryWatch(self, num: int):
        def fun(n_list ,n,k):
            ret = []
            if n <= 0 or k<=0:
                return [[]]
            for i in range(n-k+1):
                first = n_list[i]
                t = fun(n_list[i+1:],n-i-1,k-1)
                for j in range(len(t)):
                    ret.append([first]+t[j])
            return ret

        n_list = list(range(10))
        # 返回组合结果
        combinations = fun(n_list,10,num)
        rets = []
        val=[1,2,4,8,1,2,4,8,16,32]
        for item in combinations:
            h = 0
            m = 0
            for i in item:
                if i <4:
                    h += val[i]
                else:
                    m += val[i]
            if h<12 and m < 60:
                rets.append('%d:%02d' %(h,m))
        return rets
        
if __name__ == "__main__":
    a = Solution()
    print(a.readBinaryWatch(2))