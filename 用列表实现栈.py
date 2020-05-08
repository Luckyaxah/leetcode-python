class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.vals = []


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.vals.append(x)


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.vals.pop()


    def top(self) -> int:
        """
        Get the top element.
        """
        return self.vals[-1]


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.vals

    def __str__(self) -> bool:
        return self.vals.__str__()

if __name__ == "__main__":
    

# Your MyStack object will be instantiated and called as such:
    obj = MyStack()
    obj.push(1)
    obj.push(2)
    obj.push(3)
    obj.push(4)
    print(obj)
    param_2 = obj.pop()
    print(param_2)
    param_3 = obj.top()
    print(param_3)
    param_4 = obj.empty()
    print(param_4)