"""
查找和排序

题目：输入任意（用户，成绩）序列，可以获得成绩从高到低或从低到高的排列,相同成绩
都按先录入排列在前的规则处理。

示例：
jack      70
peter     96
Tom       70
smith     67

从高到低  成绩 
peter     96 
jack      70 
Tom       70 
smith     67

从低到高

smith     67

jack      70 
Tom      70 
peter     96
"""

def getList():
    line_count = input()
    line_count = int(line_count)
    asec = int(input())
    l = []
    while line_count:
        ret = input()
        l.append(ret.split())
        line_count -=1
    return l,asec

def sort(arr, asec=0):
    # 插入排序
    factor = -1 if asec==0 else 1
    for i in range(1,len(arr)):
        for j in range(i-1,-1,-1):
            if factor * int(arr[j][1])> factor * int(arr[j+1][1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]
            else:
                break
    
# if __name__ == "__main__":
l,asec = getList()
sort(l,asec)
for i in l:
    print(' '.join(i))





