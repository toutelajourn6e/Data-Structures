class MinHeap:
    def __init__(self, arr=None):
        if arr is None:
            self.heap = []
        else:
            self.heap = arr

    def heappush(self, value):
        self.heap.append(value)

        i = len(self.heap)
        parent = i // 2

        while i > 1 and self.heap[parent - 1] > self.heap[i - 1]:
            self.heap[parent - 1], self.heap[i - 1] = self.heap[i - 1], self.heap[parent - 1]
            i = parent
            parent = i // 2

    def _heapify(self, idx):
        smallest = idx
        left = (idx * 2) + 1
        right = (idx * 2) + 2

        if left >= len(self.heap):
            return
        elif right < len(self.heap):
            if self.heap[smallest] > self.heap[right]:
                smallest, right = right, smallest

        if self.heap[smallest] > self.heap[left]:
            smallest, left = left, smallest
        if smallest != idx:
            self.heap[idx], self.heap[smallest] = self.heap[smallest], self.heap[idx]
            self._heapify(smallest)

    def heapify(self):
        n = len(self.heap)
        for i in range((n // 2) - 1, -1, -1):
            self._heapify(i)

    def heappop(self):
        if not self.heap:
            raise IndexError("Heap is Empty")
        elif len(self.heap) == 1:
            return self.heap.pop()

        ret = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify(0)
        return ret


if __name__ == '__main__':
    min_heap = MinHeap()
    min_heap.heappush(5)
    min_heap.heappush(22)
    min_heap.heappush(7)
    min_heap.heappush(1)
    min_heap.heappush(4)
    min_heap.heappush(10)
    min_heap.heappush(37)
    min_heap.heappush(11)
    print(min_heap.heap)
    print(min_heap.heappop())
    print(min_heap.heappop())
    print(min_heap.heappop())
    print(min_heap.heappop())
    min_heap.heappush(2)
    min_heap.heappush(57)
    print(min_heap.heap)
    print(min_heap.heappop())
    print(min_heap.heappop())
    print(min_heap.heappop())
    print('-------------------------------------')
    test_arr = [15, 2, 7, 33, 4, 9, 22, 45, 5]
    test_arr = MinHeap(test_arr)
    test_arr.heapify()
    print(test_arr.heap)
    print(test_arr.heappop())
    print(test_arr.heappop())
    print(test_arr.heappop())
    test_arr.heappush(13)
    test_arr.heappush(81)
    print(test_arr.heappop())
    print(test_arr.heappop())
    print(test_arr.heap)

# [1, 4, 7, 11, 5, 10, 37, 22]
# 1
# 4
# 5
# 7
# [2, 10, 22, 37, 11, 57]
# 2
# 10
# 11
# -------------------------------------
# [2, 4, 7, 5, 15, 9, 22, 45, 33]
# 2
# 4
# 5
# 7
# 9
# [13, 15, 22, 33, 45, 81]
