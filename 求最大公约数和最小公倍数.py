# x=int(input("请输入一个整数："))
# y=int(input("请再输入一个整数："))
x, y = 8, 12
m,n=x,y
gys=1
gbs=0
for i in range(2,100):
    while x%i==0 and y%i==0:
        gys=gys*i
        x=x/i
        y=y/i
gbs=m*n/gys
print("最大公约数是:{}，最小公倍数是：{}".format(gys,gbs))