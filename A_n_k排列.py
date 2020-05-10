class Solution:
    def A_n_k(self, num: int):
        l = list(range(10))
        def help(l, n):
            if n == 1:
                return [[i] for i in l]
            ret = []
            for i,v in enumerate(l):
                rets = help(l[:i]+l[i+1:], n-1)
                for item in rets:
                    ret.append([v] +item)
            return ret
        ret = help(l, num)
        return ret

if __name__ == "__main__":
    a = Solution()
    print(a.A_n_k(2))