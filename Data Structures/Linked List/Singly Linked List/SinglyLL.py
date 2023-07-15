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

    def search_value(self, target):
        if self.is_empty():
            return print("Linked List is Empty")
        node = self.head
        for i in range(self.size):
            if node.value == target:
                return i
            node = node.next
        return None

    def search_idx(self, idx):
        if self.is_empty():
            return print("Linked List is Empty")
        elif idx < 0 or idx >= self.size:
            raise IndexError("Linked List index out of range")
        else:
            node = self.head
            for i in range(idx):
                node = node.next
            return node.value

    def add_last(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def add_first(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1

    def insert(self, idx, value):
        if idx < 0 or idx > self.size:
            raise IndexError("Linked List index out of range")
        if idx == 0:
            return self.add_first(value)
        elif idx == self.size:
            return self.add_last(value)
        else:
            new_node = Node(value)
            node = self.head
            for i in range(idx - 1):
                node = node.next
            new_node.next = node.next
            node.next = new_node
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

    def remove(self, idx):
        if idx < 0 or idx > self.size:
            raise IndexError("Linked List assignment index out of range")
        if idx == 0:
            return self.delete_first()
        elif idx == self.size:
            return self.delete_last()
        else:
            node = self.head
            for i in range(idx - 1):
                node = node.next
            del_node = node.next
            node.next = del_node.next
            del_node.next = None
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
    s_list.add_last(3)
    s_list.add_last(5)
    s_list.delete_first()
    s_list.add_first(1)
    s_list.delete_last()
    s_list.add_first(7)
    s_list.add_last(14)
    print(s_list.get_size())
    s_list.traverse()
    print(s_list.search_value(7))
    s_list.insert(1, 5)
    s_list.remove(2)
    s_list.insert(2, 2)
    s_list.traverse()
    print(s_list.search_idx(3))
    print(s_list.get_size())

# True
# 3
# data > 7
# data > 1
# data > 14
# 0
# data > 7
# data > 5
# data > 2
# data > 14
# 14
# 4
