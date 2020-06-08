import math
def maxLcpsLength(s):
    if s == None or len(s) == 0:
        return 0
    str1 = manacherString(s)
    # 存的时回文半径的大小
    pArr = [None] * len(str1)
    C = -1
    R = -1 # 讲述时，R表示最右的扩成功的位置。在这里的代码中R表示最右扩成功的位置的下一个位置。
    maxValue = -math.inf
    for i in range(len(str1)):
        # i位置扩出来的答案。i位置扩大的半径至少是多少
        pArr[i] = min(pArr[2*C-i], R-i) if R>i else 1 # R>i 表示i在R内
        # 如果i在R内，i至少要扩的区域是，i到R的距离和i‘的回文半径较小的那一个。

        while i + pArr[i] < len(str1) and i - pArr[i] > -1:
            # 在左边不越界，右边不越界的情况下
            if str1[i + pArr[i]] == str1[i-pArr[i]]:
                pArr[i] += 1
            else:
                break
        if i + pArr[i] > R:
            R = i + pArr[i]
            C = i
        maxValue = max(maxValue, pArr[i])
        # 原始串的大小，回文半径-1，或回文直径//2
    return maxValue-1

def manacherString(s):
    return '#'+'#'.join(list(s))+'#'

if __name__ == "__main__":
    a = '1221312214'
    print(maxLcpsLength(a))