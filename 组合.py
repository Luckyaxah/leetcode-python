class Solution:
    def combine(self, n: int, k: int):
        n_list = list(range(1,n+1))
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
        return fun(n_list,n,k)
            
                
if __name__ == "__main__":
    a = Solution()
    print(a.combine(4,2))
    pass