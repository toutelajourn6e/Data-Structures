class Queue:
    def __init__(self, capacity):
        self.size = self.front = 0
        self.rear = capacity - 1
        self.capacity = capacity
        self.array = [None] * capacity


    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0


    def enqueue(self, value):
        if self.is_full():
            print("Queue is Full")
            return
        self.rear = (self.rear + 1) % self.capacity
        self.array[self.rear] = value
        self.size += 1


    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is Empty")
        value = self.array[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return value


    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is Empty")
        return self.array[self.front]


if __name__ == "__main__":
    my_queue = Queue(10)
    print(my_queue.is_empty())
    my_queue.enqueue(6)
    my_queue.enqueue(1)
    my_queue.enqueue(2)
    my_queue.enqueue(9)
    print(my_queue.dequeue())
    print(my_queue.dequeue())
    my_queue.enqueue(8)
    print(my_queue.dequeue())
    print(my_queue.dequeue())
    print(my_queue.peek())
    print(my_queue.dequeue())
    print(my_queue.is_full())
    print(my_queue.is_empty())


# True
# 6
# 1
# 2
# 9
# 8
# 8
# False
# True

