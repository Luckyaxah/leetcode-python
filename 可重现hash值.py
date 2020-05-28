# 注意可变数据类型不可进行hash映射，因为相当于映射内存地址
# 对于python3
# 相同字符串在同一次运行时的哈希值是相同的，但是不同次运行的哈希值不同。
# 这是由于Python的字符串hash算法有一个启动时随机生成secret prefix/suffix的机制，
# 存在随机化现象：对同一个字符串输入，不同解释器进程得到的hash结果可能不同。
# 因此当需要做可重现可跨进程保持一致性的hash，需要用到hashlib模块。
# https://www.cnblogs.com/abdm-989/p/11329122.html

import hashlib
a =hashlib.md5()
a.update(b'abc')
a.update(b' efg')
# a
# <md5 HASH object @ 0x10db1c6c0>
a.digest()
# b'\x11\xf2\x8f-m\r6\xe4\x9a\x07\x9aw\x8ar\xae\xed'
a.hexdigest()
# '11f28f2d6d0d36e49a079a778a72aeed'
b = hashlib.md5()
b.update(b'abc efg')
b.hexdigest()
# '11f28f2d6d0d36e49a079a778a72aeed'