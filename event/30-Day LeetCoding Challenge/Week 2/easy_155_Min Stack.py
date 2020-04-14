class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.min = []
        self.data_ptr = -1
        self.min_ptr = -1

    def push(self, x: int) -> None:
        self.data.append(x)
        self.data_ptr += 1

        if not self.min:
            self.min.append(x)
        else:
            if x < self.min[self.min_ptr]:
                self.min.append(x)
            else:
                self.min.append(self.min[self.min_ptr])
        self.min_ptr += 1

    def pop(self) -> None:
        if self.data:
            self.data.pop()
            self.data_ptr -= 1

        if self.min:
            self.min.pop()
            self.min_ptr -= 1

    def top(self) -> int:
        return self.data[self.data_ptr]

    def getMin(self) -> int:
        return self.min[self.min_ptr]


if __name__ == "__main__":
    try:
        obj = MinStack()
        print(obj.push(-2))
        print(obj.push(0))
        print(obj.push(-3))
        print(obj.getMin())
        print(obj.pop())
        print(obj.top())
        print(obj.getMin())
        # None, None, None, -3, None, 0, -2
    except Exception as e:
        print(e)
    finally:
        pass


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
