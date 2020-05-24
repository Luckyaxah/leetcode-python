
from queue import Queue
# LILO
q = Queue()
q.put(0)
q.put(1)
q.put(2)
print('LILO队列',q.queue)  #查看队列中的所有元素
print(q.get())  #返回并删除队列头部元素
print(q.queue)