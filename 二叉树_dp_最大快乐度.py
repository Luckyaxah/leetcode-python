# 多叉树节点
class Node:
    def __init__(self, a):
        self.happy = a
        self.nexts = []

def maxHappy(head):
    pass

class Info:
    def __init__(self, no, yes):
        self.headNo = no
        self.headYes = yes


def process(x):
    if not x.nexts:
        return Info(0, x.happy)
    headNo = 0
    headYes = x.happy
    for everyNext in x.nexts:
        cur = process(everyNext)
        headYes += cur.headNo
        headNo += max(cur.headNo, cur.headYes)
    return Info(headNo, headYes)

    
    
