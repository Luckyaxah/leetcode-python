def allSubSeq(str1):
    ret = []
    if str1 == None:
        return ret
    if len(str1) == 0:
        ret.append('')
        return ret
    process(str1, 0, '', ret)
    return ret

def process(str1, index ,path, ret):
    """
    在str[0...index-1]的沿途决定由path记录
    str[index...]中每个字符都可选择或不选择，生成的结果放入ret中
    """
    if index == len(str1):
        ret.append(path)
    else:
        process(str1, index+1, path, ret)
        process(str1, index+1, path+str1[index], ret)


if __name__ == "__main__":
    a = allSubSeq('abc')
    print(a)
    
