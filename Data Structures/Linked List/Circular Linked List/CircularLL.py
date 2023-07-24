class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get_size(self):
        return self.size

    def is_empty(self):
        return not bool(self.size)

    def first(self):
        return self.head.value

    def insert(self, value):
        node = Node(value)
        if self.is_empty():
            node.next = node
            self.head = node
        else:
            node.next = self.head.next
            self.head.next = node
        self.size += 1

    def delete(self):
        if self.is_empty():
            raise IndexError("Linked List is Empty")
        node = self.head.next
        if self.size == 1:
            node.next = None
            self.head = None
        else:
            self.head.next = node.next
            node.next = None
        self.size -= 1

    def traverse(self):
        if self.is_empty():
            return print("Linked List is Empty")
        node = self.head.next
        while node != self.head:
            print('data >', node.value)
            node = node.next
        print('head >', self.head.value)


if __name__ == '__main__':
    c_list = CircularLinkedList()
    print(c_list.is_empty())
    c_list.insert(2)
    c_list.insert(6)
    c_list.insert(9)
    c_list.insert(4)
    c_list.traverse()
    c_list.insert(1)
    print(c_list.first())
    c_list.delete()
    c_list.delete()
    c_list.traverse()
    print(c_list.get_size())

# True
# data > 4
# data > 9
# data > 6
# head > 2
# 2
# data > 9
# data > 6
# head > 2
# 3
