"""
在python3中使用自定义函数做排序需要用到functools.cmp_to_key
"""

class A:
    def __init__(self,vals):
        self.a = vals[0]
        self.b = vals[1]

def fun1(x,y):
    if x.a!=y.a:
        return x.a-y.a
    else:
        return x.b-y.b


if __name__ == "__main__":
    import functools
    a1 = [1,2,3,2,5,2,1]
    b1 = [4.1,2.1,2,3.0,1.3,6.0,4.0]
    l = [A(item) for item in zip(a1,b1)]
    l.sort(key = functools.cmp_to_key(fun1))
    for i in l:
        print(i.a,i.b)