class Solution:
    def getRow(self, numRows: int):
        def fun(n):
            if n == 0:
                return []
            if n == 1:
                return [1]
            previous =fun(n-1)
            temp = [1]
            for i in range(n-2):
                temp.append(previous[i]+ previous[i+1])
            temp.append(1)
            return temp
        return fun(numRows+1)
if __name__ == "__main__":
    a = Solution()
    ret = a.getRow(0)
    print(ret)
