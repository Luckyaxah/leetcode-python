from functools import wraps
def decorator(func):
    @wraps(func)
    def wraper(*args, **kwargs):
        print(type(args), args)
        print(type(kwargs), kwargs)
        print('hey, you')
        ret = func(*args, **kwargs)
        print('processing', ret)
        print('ok, done')
        return ret
    
    return wraper

@decorator
def fun1(x, y, extraneous=1):
    return x+y

@decorator
def fun2(x, y, extraneous=2):
    return x-y

print('result:', fun1(1,2))
print('result:', fun2(1,2))