class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


class DoublyLinkedList:
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
            if idx <= self.size // 2:
                node = self.head
                for i in range(idx):
                    node = node.next
            else:
                node = self.tail
                for i in range(idx):
                    node = node.prev
        return node.value

    def add_last(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.size += 1

    def add_first(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
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
            if idx <= self.size // 2:
                node = self.head
                for i in range(idx):
                    node = node.next
            else:
                node = self.tail
                for i in range(self.size - (idx + 1)):
                    node = node.prev
            new_node.prev = node.prev
            new_node.next = node
            node.prev = new_node
            new_node.prev.next = new_node
        self.size += 1

    def delete_last(self):
        if self.is_empty():
            print("Linked List is Empty")
            return
        if self.get_size() == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1

    def delete_first(self):
        if self.is_empty():
            print("Linked List is Empty")
            return
        if self.get_size() == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1

    def remove(self, idx):
        if idx < 0 or idx > self.size:
            raise IndexError("Linked List assignment index out of range")
        if idx == 0:
            return self.delete_first()
        elif idx == self.size:
            return self.delete_last()
        else:
            if idx <= self.size // 2:
                node = self.head
                for i in range(idx):
                    node = node.next
            else:
                node = self.tail
                for i in range(self.size - (idx + 1)):
                    node = node.prev
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next = None
            node.prev = None
        self.size -= 1

    def reverse(self):
        temp = None
        node = self.head
        self.tail = node
        while node is not None:
            temp = node.prev
            node.prev = node.next
            node.next = temp
            node = node.prev
        if temp is not None:
            self.head = temp.prev

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
    d_list = DoublyLinkedList()
    print(d_list.is_empty())
    d_list.insert(0, 5)
    d_list.add_last(12)
    d_list.add_last(23)
    d_list.add_first(3)
    d_list.add_first(8)
    d_list.insert(1, 9)
    d_list.delete_last()
    d_list.remove(1)
    d_list.traverse()
    print(d_list.search_idx(2))
    print(d_list.search_value(12))
    d_list.reverse()
    d_list.traverse()
    print(d_list.head.value, d_list.tail.value)

# True
# data > 8
# data > 3
# data > 5
# data > 12
# 5
# 3
# data > 12
# data > 5
# data > 3
# data > 8
# 12 8