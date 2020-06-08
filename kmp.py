def getIndexOf(s, m):
    if s == None or m == None or len(m)< 1 or len(s)<len(m):
        return -1
    str1 = list(s)
    str2 = list(m)
    x = 0 # str1中比对到的位置
    y = 0 # str2中比对到的位置
    next_list = getNextArray(str2) # 这个next_list既表示长度，也表示你该往哪儿跳
    while x < len(str1) and y< len(str2):
        # 跳出while的条件，要么x越界，要么y越界。y越界说明找到了，x越界说明没找到
        if str1[x] == str2[y]:
            x += 1
            y += 1
        elif next_list[y] == -1:
            x += 1
        else:
            y = next_list[y]
    return x-y if y == len(str2) else -1

def getNextArray(ms):
    if len(ms) == 1:
        return [-1]
    next_list = [None]*len(ms)
    next_list[0] = -1
    next_list[1] = 0
    i = 2
    cn = 0
    # cn位置，是当前和i-1位置比较的字符
    while i < len(next_list):
        if ms[i-1] == ms[cn]:
            cn += 1
            next_list[i] =  cn
            i += 1
        elif cn>0:
            cn = next_list[cn]
        else:
            next_list[i] = 0
            i+= 1
    return next_list

if __name__ == "__main__":
    s = 'abacabxfabacabaE'
    print(getNextArray(s))

    s1 = 'abacaaabcsexaaas'
    s2 = 'abcs'
    print(getIndexOf(s1,s2))