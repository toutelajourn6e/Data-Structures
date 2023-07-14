class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get_size(self):
        return self.size

    def is_empty(self):
        return not bool(self.size)

    def search(self, target):
        if self.is_empty():
            print("Linked List is Empty")
            return
        node = self.head
        for i in range(self.size):
            if node.value == target:
                return i, node
            node = node.next
        return None

    def insert_last(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def insert_first(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1

    def delete_last(self):
        if self.is_empty():
            print("Linked List is Empty")
            return
        node = self.head
        if self.get_size() == 1:
            self.head = None
            self.tail = None
        else:
            while node.next != self.tail:
                node = node.next
            self.tail = node
            node.next = None
        self.size -= 1

    def delete_first(self):
        if self.is_empty():
            print("Linked List is Empty")
            return
        node = self.head
        if self.get_size() == 1:
            self.head = None
            self.tail = None
        else:
            self.head = node.next
            node.next = None
        self.size -= 1

    def traverse(self):
        if self.is_empty():
            print("Linked List is Empty")
            return
        node = self.head
        while node.value:
            print('data >', node.value)
            node = node.next
            if node == self.tail.next:
                break


if __name__ == '__main__':
    s_list = SinglyLinkedList()
    print(s_list.is_empty())
    s_list.insert_last(3)
    s_list.insert_last(5)
    s_list.delete_first()
    s_list.insert_first(1)
    s_list.delete_last()
    s_list.insert_first(7)
    s_list.insert_last(14)
    print(s_list.get_size())
    s_list.traverse()
    print(s_list.search(7))

# True
# 3
# data > 7
# data > 1
# data > 14
# (0, <__main__.Node object at 0x7fe7502d7d00>)
