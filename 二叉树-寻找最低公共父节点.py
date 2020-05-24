

class Info:
    def __init__(self, findresult, findO1, findO2):
        self.findAns = findresult
        self.findO1 = findO1
        self.findO2 = findO2

def lowestCommon1(head, o1, o2):
    def process(head, o1, o2):
        if not head:
            return Info(None, False, False)
        leftInfo = process(head.left, o1, o2)
        rightInfo = process(head.right, o1, o2)
        if leftInfo.findAns:
            return leftInfo
        if rightInfo.findAns:
            return rightInfo
        findO1 = head == o1
        findO2 = head == o2
        if leftInfo.findO1 or rightInfo.findO1:
            if findO2:
                return Info(head, True, True)
            else:
                return Info(head, True, False)
        if leftInfo.findO2 or rightInfo.findO2:
            if findO1:
                return Info(head, True, True)
            else:
                return Info(head, False, True)
        return Info(None, False, False)
        
    ret = process(head, o1, o2)
    return ret.findAns


def lowestCommon(head, o1, o2):
    def process(head, o1, o2):
        if not head:
            return Info(None, False, False)
        leftInfo = process(head.left, o1, o2)
        rightInfo = process(head.right, o1, o2)
        if leftInfo.findAns:
            return leftInfo
        if rightInfo.findAns:
            return rightInfo
        findO1 = False
        findO2 = False
        if leftInfo.findO1 or rightInfo.findO1 or head == o1:
            findO1 = True
        if leftInfo.findO2 or rightInfo.findO2 or head == o2:
            findO2 = True
        if findO1 and findO2:
            return Info(head, True, True)
        return Info(None, findO1, findO2)
    ret = process(head, o1, o2)
    return ret.findAns
