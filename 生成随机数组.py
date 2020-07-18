import random
# 对数器使用
def random_list(start = 1, end = 10, length =(1,10)):
    start = 1
    end = 10
    size = random.randint(length[0], length[1])
    ret = [random.randint(start, end) for i in range(size)]
    return ret