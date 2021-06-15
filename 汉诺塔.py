# 原理
# 一共有三个区域，初始状态时所有圆盘在区域一，按升序排列。
# 每次移动一个圆盘将所有圆盘移动到区域三。
# 要求：序号小的圆盘不能在序号大的圆盘下面。
def fun(n):
    arr = [i for i in range(n)]
    def help(arr, p1, p2, p3):
        # p1是起点，p2是终点，p3是另一个区域
        if len(arr) == 1:
            print('将%d从%s移动到%s' % (arr[0], p1, p2))
            return
        help(arr[:-1], p1, p3, p2)
        help([arr[-1]], p1, p2, p3)
        help(arr[:-1], p3, p2, p1)
    help(arr, 'A','C','B')
fun(5)