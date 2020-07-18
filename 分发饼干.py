def findContentChildren1(g, s) -> int:
    # 暴力递归方法
    def process(g,s):
        if (not g) or (not s):
            return 0
        # p0表示第一块饼干不被分配
        p0 = process(g, s[1:])
        max_p = p0
        # 之后表示第一块饼干被分配，返回能满足孩子的最大数目
        for i in range(len(g)):
            if s[0] < g[i]:
                continue
            p1 = process(g[:i]+g[i+1:], s[1:]) +1
            max_p = max(max_p, p1)
        return max_p
    return process(g,s)

def findContentChildren(g, s) -> int:
    g.sort()
    s.sort()
    ret = 0
    i, j = 0, 0
    while i < len(g) and j < len(s):
        while j< len(s) and s[j] < g[i]: j += 1
        if j < len(s): ret += 1
        i += 1
        j += 1
    return ret
                    



if __name__ == "__main__":

    from 生成随机数组 import random_list
    g = random_list()
    s = random_list()
    print(g, s)
    print(findContentChildren1(g,s))
    print(findContentChildren(g,s))
       
    