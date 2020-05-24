"""
对于一个由0..n的所有数按升序组成的序列，我们要进行一些筛选，
每次我们取当前所有数字中从小到大的第奇数位个的数，并将其丢弃。
重复这一过程直到最后剩下一个数。请求出最后剩下的数字。
"""

def getLast(l):
    pos = 0
    while len(l)>1:
        l.pop(pos)
        pos = (pos+1 ) % len(l)
    return l[0]


if __name__ == "__main__":
    
    a = [1,2,3,4]
    print(getLast(a))