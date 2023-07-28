class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.size = 0

    def get_size(self):
        return self.size

    def is_empty(self):
        return not bool(self.size)



    def enqueue(self, value):
        while self.stack1:
            self.stack2.append(self.stack1.pop())

        self.stack1.append(value)

        while self.stack2:
            self.stack1.append(self.stack2.pop())

        self.size += 1


    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        self.size -= 1
        return self.stack1.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is Empty")
        return self.stack1[-1]


    def print_queue(self):
        if self.is_empty():
            return print("Queue is Empty")
        for i in range(len(self.stack1)-1, -1, -1):
            print('data >', self.stack1[i])


if __name__ == "__main__":
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