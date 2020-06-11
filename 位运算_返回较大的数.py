
"""
In [3]: bin(-1 & 0xffffffff)                                                                          
Out[3]: '0b11111111111111111111111111111111'

In [4]: int('0b11111111111111111111111111111111',2)                                                   
Out[4]: 4294967295

In [7]: 2**32-1                                                                                       
Out[7]: 4294967295

In [9]: int(bin(-3 & 0xffffffff),2)                                                                   
Out[9]: 4294967293

In [10]: 2**32-3                                                                                      
Out[10]: 4294967293

a = bin(-3)
print(a)

a = bin(3)
print(a)
 
b = bin(-3 & 0xffffffff)
print(b)
 
c = bin(0xfffffffd)
print(c)
 
//输出
//-0b11
//0b11
//0b11111111111111111111111111111101
//0b11111111111111111111111111111101

但是在c/c++/java里面负数都是以补码的形式进行存储的，
《计算机原理》显示，计算机内部采用2的补码（Two's Complement）表示负数。
"""


def get32bin(n):
    """
    In [47]: get32bin(2**32-1)                                                                            
    Out[47]: '0b11111111111111111111111111111111'
    In [48]: get32bin(-1)                                                                                 
    Out[48]: '0b11111111111111111111111111111111'
    """
    return bin(n & 0xffffffff)

def flip(n):
    # 1->0, 0->1
    return n^1

def sign(n):
    """
    如果n是负数，返回0，如果n是非负数，返回1
    """
    if n<-2**31 or n>2**31-1:
        print('不是int32型整数')
        return
    # 这里输入的n只能是-2**31～2**31-1这么多
    # 在java中，将n的符号位移到最右边，和1与
    return flip( (n>>31) & 1 )

# a-b的值如果溢出了，该函数不正确
def getMax1(a,b):
    c = a-b
    scA = sign(c)
    scB = flip(scA)
    return a * scA + b* scB

def getMax2(a,b):
    c = a-b
    sa = sign(a)
    sb = sign(b)
    sc = sign(c)
    difSab = sa^sb # a和b符号不同时为1
    sameSab = flip(difSab) # a和b符号相同时为1
    returnA = difSab * sa + sameSab *sc # ab符号不同，且a为正时，返回a。ab符号相同时，如果sc为正返回c
    returnB = flip(returnA)
    return a * returnA + b* returnB