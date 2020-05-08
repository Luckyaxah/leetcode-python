#
# 
# @param n int整型 水桶的个数
# @param q int整型 询问的次数
# @param a int整型一维数组 n个水桶中初始水的体积
# @param p int整型一维数组 每次询问的值
# @return int整型一维数组
#
class Solution:
    def solve(self , n , q , a , p ):
        # write code here
        a.sort()
        # print(a)

        ret = []
        for i in range(q):
            k = p[i]
            minimal =-1
            j1 =0
            Sum = sum(a[0:k])
            for i1 in range(n-k+1):
                if i1>0:
                    Sum = Sum-a[i1-1]+a[k+i1-1]
                diff = a[i1+k-1]*k - Sum
                if minimal == -1 or minimal > diff:
                    minimal = diff
                    j1 = i1
            ret.append(minimal)
            if minimal>0:
                for j in range(k):
                    a[j1+j] = a[j1+k-1]
        return ret

if __name__ == '__main__':

    Sol = Solution()
    case1 = [50,10,[278,125,679,818,337,683,245,67,922,43,310,505,254,951,378,733,373,643,170,632,711,766,256,620,570,51,494,907,388,126,580,823,485,693,969,931,209,455,533,414,318,777,862,102,742,257,550,706,492,968],[28,15,19,38,27,13,23,38,11,30],[6189,0,0,5748,0,0,0,0,0,0]]
    case2 = [4,3,[1,2,3,4],[2,2,4],[1,0,5]]
    cases =[case1,case2]
    for i in range(len(cases)):
        ret = Sol.solve(*cases[i][:-1])
        result = cases[i][-1]
        try:
            assert ret == result
            retStr ='Correct'
        except:
            retStr ='Wrong'
        print('case'+str(i+1)+' : ' + retStr)
