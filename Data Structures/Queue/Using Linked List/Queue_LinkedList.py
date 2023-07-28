class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get_size(self):
        return self.size

    def is_empty(self):
        return not bool(self.size)

    def enqueue(self, value):
        node = Node(value)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty list")
        node = self.head
        self.head = self.head.next
        node.next = None
        self.size -= 1
        return node.value

    def peek(self):
        return self.head.value


    def print_queue(self):
        if self.is_empty():
            return print("Queue is Empty")
        node = self.head
        while node.next is not None:
            print('data >', node.value)
            node = node.next
        print('data >', self.tail.value)


if __name__ == '__main__':
    my_queue = Queue()
    print(my_queue.is_empty())
    my_queue.enqueue(23)
    my_queue.enqueue(5)
    my_queue.enqueue(17)
    print(my_queue.dequeue())
    print(my_queue.dequeue())
    my_queue.enqueue(3)
    my_queue.enqueue(9)
    my_queue.print_queue()
    print(my_queue.peek())
    print(my_queue.get_size())

# True
# 23
# 5
# data > 17
# data > 3
# data > 9
# 17
# 3