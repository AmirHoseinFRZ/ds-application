class Stack:
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        self.array = []

    def is_empty(self):
        return True if self.top == -1 else False

    def peek(self):
        return self.array[-1]

    def pop(self):
        if not self.is_empty():
            self.top -= 1
            return self.array.pop()
        else:
            return "$"

    def push(self, op):
        self.top += 1
        self.array.append(op)

    def not_greater(self, i):
        precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
        try:
            print(0)
            a = precedence[i]
            print(i, a)
            b = precedence[self.peek()]
            print("peek", b)
            return True if a <= b else False
        except KeyError:
            return False