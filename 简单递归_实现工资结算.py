def get_pay(n):
    if n == 1:
        money = 20
        total = 20
        print('第%d天能拿%d' % (n,money))
        return money, total
    money, total = get_pay(n-1)
    money *= 2
    total += money
    print('第%d天能拿%d' % (n, money))
    return money, total

print(get_pay(20))