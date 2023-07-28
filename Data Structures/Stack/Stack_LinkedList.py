class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def get_size(self):
        return self.size

    def is_empty(self):
        return not bool(self.size)

    def push(self, value):
        node = Node(value)
        if self.is_empty():
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty list")
        node = self.head
        self.head = node.next
        self.size -= 1
        return node.value

    def peek(self):
        if self.is_empty():
            return print("Stack is Empty")
        return self.head.value

    def print_stack(self):
        if self.is_empty():
            return print("Stack is Empty")
        node = self.head
        while node is not None:
            print('data >', node.value)
            node = node.next


if __name__ == '__main__':
    my_stack = Stack()
    print(my_stack.is_empty())
    my_stack.push(5)
    my_stack.push(8)
    my_stack.push(10)
    print(my_stack.peek())
    my_stack.pop()
    my_stack.pop()
    print(my_stack.peek())
    my_stack.push(1)
    my_stack.push(3)
    my_stack.push(9)
    my_stack.print_stack()
    print(my_stack.peek())
    print(my_stack.get_size())


# True
# 10
# 5
# data > 9
# data > 3
# data > 1
# data > 5
# 9
# 4
