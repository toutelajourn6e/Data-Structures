class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return not bool(self.size)

    def append(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def append_left(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1

    def popleft(self):
        if self.is_empty():
            print("Linked List is Empty")
            return

        node = self.head
        self.head = node.next
        node.next = None
        self.size -= 1
        return node.value

    def traverse(self):
        node = self.head
        while node.value:
            print('data >', node.value)
            node = node.nextf
            if node == self.tail.next:
                break


if __name__ == '__main__':
    s_list = SinglyLinkedList()
    s_list.append(3)
    s_list.append(5)
    s_list.append(2)
    s_list.traverse()
    print(s_list.popleft())
    print(s_list.is_empty())
    s_list.traverse()
