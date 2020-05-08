class Solution:
    def generate(self, numRows: int):
        if numRows == 0:
            return []
        ret = []
        def fun(n):
            if n == 1:
                ret.append([1])
                return
            fun(n-1)
            temp = [1]
            for i in range(n-2):
                temp.append(ret[-1][i]+ ret[-1][i+1])
            temp.append(1)
            ret.append(temp)
        fun(numRows)
        return ret
if __name__ == "__main__":
    a = Solution()
    ret = a.generate(4)
    for row in ret:
        print(row)