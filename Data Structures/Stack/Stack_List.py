class Stack:
    def __init__(self):
        self.stack = []

    def get_size(self):
        return len(self.stack)

    def is_empty(self):
        return not bool(self.stack)

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        item = self.stack.pop()
        return item

    def peek(self):
        return self.stack[-1]

    def print_stack(self):
        if self.is_empty():
            print("Stack is Empty")
            return
        for i in range(len(self.stack) - 1, -1, -1):
            print('data >', self.stack[i])


if __name__ == '__main__':
    my_stack = Stack()
    print(my_stack.is_empty())
    my_stack.push(4)
    my_stack.push(2)
    my_stack.push(7)
    my_stack.push(5)
    my_stack.print_stack()
    my_stack.pop()
    print(my_stack.peek())
    my_stack.push(9)
    print(my_stack.get_size())

# True
# data > 5
# data > 7
# data > 2
# data > 4
# 7
# 4