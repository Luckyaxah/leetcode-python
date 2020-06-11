# 提取二进制数字中最右侧的1
# ans = n & (~n +1)

def fun(n):
    ans = n & (~n+1)
    return ans == n

def fun1(n):
    ans = n & (n-1)
    return ans == 0

def fun4(n):
    n = n & 0xffffffff
    # print((n & 0x55555555 !=0 ))
    return (n & (n-1) == 0) and (n & 0x55555555 !=0 )
  
if __name__ == "__main__":
    print(fun(2),fun1(2))
    print(fun(3),fun1(3))
    print(fun4(3))
    print(fun4(2))
    print(fun4(4))
    print(fun4(8))