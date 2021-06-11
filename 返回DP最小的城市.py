#coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。
import sys
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())

    edges = []
    for i in range(n-1):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # line = data[i]
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        edges.append(values)

    d1 = {}
    for edge in edges:
        # d1.get(edge[0],[]).append(edge[1])
        # d1.get(edge[1],[]).append(edge[0])

        if edge[0] in d1:
            d1[edge[0]].append(edge[1])
        else:
            d1[edge[0]] = [edge[1]]
        if edge[1] in d1:
            d1[edge[1]].append(edge[0])
        else:
            d1[edge[1]] = [edge[0]]

    def fun(cities, ncity):
        nums = []
        for city in cities:
            visited = [ncity]
            fun1(visited, city)
            nums.append( len(visited)-1 )
        return max(nums)

    def fun1(visited, city):
        if city in visited:
            return
        visited.append(city)
        for c in d1[city]:
            fun1(visited, c)


    # 0~n-1 表示n个城市
    dp = [0 for i in range(n)]
    for i in range(1, n+1):
        dp[i-1] = fun(d1[i], i)
    _min = min(dp)
    index = ''
    for i in range(n):
        if dp[i] == _min:
            index += str(i+1) + ' '

    print(index[:-1])
    
    
    




