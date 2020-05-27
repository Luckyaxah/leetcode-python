

def process(str1, i):
    if i== len(str1):
        return 1
    if str1[i] == '0':
        return 0
    if str1[i] == '1':
        res = process(str1, i+1)
        if i+1 < len(str1):
            res += process(str1, i+2)
        return res
    if str1[i] == '2':
        res = process(str1, i+1)
        if i+1 < len(str1) and str1[i+1]<='6' and str1[i+1]>='0':
            res += process(str1, i+2)
        return res
    return process(str1, i+1)

if __name__ == "__main__":
    a = "111"
    print(process(a,0))