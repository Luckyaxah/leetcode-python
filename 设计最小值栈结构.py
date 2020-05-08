
class MinStack:
    def __init__(self):
        self.items = []
    def push(self, item):
        if len(self.items) == 0:
            self.items.append([item,item])
            return
        cur_min = self.items[-1][1]
        new_min = min(cur_min,item)
        self.items.append([item,new_min])
        
    def pop(self):
        self.items.pop()
    def getMin(self):
        return self.items[-1][1]
    def top(self):
        return self.items[-1][0]
    def size(self):
        return len(self.items)

if __name__ == "__main__":

    minStack = MinStack()
    print(minStack.items)
    minStack.push(-2)
    print(minStack.items)
    minStack.push(0)
    print(minStack.items)
    minStack.push(-3)
    print(minStack.items)
    minStack.getMin()
    print(minStack.getMin())
    print(minStack.items)

    # minStack.pop()
    # print(minStack.items)
    # minStack.top()
    # print(minStack.items)
    # minStack.getMin()
    # print(minStack.getMin())
