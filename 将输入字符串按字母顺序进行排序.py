
"""
编写一个程序，将输入字符串中的字符按如下规则排序。
"""
from 堆排序ver2 import heapSort
def sortStr(str1):
    l = list(str1)
    def getOrder(char:str):
        return ord(char.lower())
    help_arr = []
    for i in str1:
        if i.lower()>='a' and i.lower()<='z':
            help_arr.append(i)
    heapSort(help_arr, order_fun=getOrder )
    j = 0
    
    for i in range(len(str1)):
        if l[i].lower()>='a' and l[i].lower()<='z':
            l[i]= help_arr[j]
            j +=1
    return ''.join(l)
    


if __name__ == "__main__":
    str1 = 'A Famous Saying: Much Ado About Nothing (2012/8).'
    ret = sortStr(str1)
    print(ret)