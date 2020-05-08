from 用列表实现栈 import MyStack

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = MyStack()
        self.helper = MyStack()

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack.push(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        while not self.stack.empty():
            self.helper.push(self.stack.pop())
        ret = self.helper.pop()
        while not self.helper.empty():
            self.stack.push(self.helper.pop())
        return ret


    def peek(self) -> int:
        """
        Get the front element.
        """
        while not self.stack.empty():
            self.helper.push(self.stack.pop())
        ret = self.helper.top()
        while not self.helper.empty():
            self.stack.push(self.helper.pop())
        return ret


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.stack.empty()

    def __str__(self) -> str:
        """
        Returns whether the queue is empty.
        """
        return self.stack.__str__()

if __name__ == "__main__":
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    print(queue)
    queue.pop()
    print(queue)
    print(queue.peek())
    queue.push(4)
    print(queue)
    print(queue.empty())

