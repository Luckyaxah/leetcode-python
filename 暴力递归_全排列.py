def getAllC(s):
    ans = []
    charList = list(s) # 包含重复字符
    process(charList, "", ans)
    return ans
def process(charList, path, ans):
    if not charList:
        ans.append(path)
        return
    for i in range(len(charList)):
        pick = path+ charList[i]
        _next = list(charList)
        _next.pop(i)
        process(_next, pick, ans)

def getAllC_norepeat(s):
    ans = []
    charList = list(s) # 包含重复字符
    process1(charList, "", ans)
    return ans

def process1(charList, path, ans):
    if not charList:
        ans.append(path)
        return
    picks = set()
    for i in range(len(charList)):
        if  not charList[i] in picks:
            picks.add(charList[i])
            pick = path+ charList[i]
            _next = list(charList)
            _next.pop(i)
            process1(_next, pick, ans)

if __name__ == "__main__":
    ret = getAllC('aac')
    print(ret)
    ret = getAllC_norepeat('aac')
    print(ret)