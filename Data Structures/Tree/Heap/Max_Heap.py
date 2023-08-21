class MaxHeap:
    def __init__(self, arr=None):
        if arr is None:
            self.heap = []
        else:
            self.heap = arr

    def heappush(self, value):
        self.heap.append(value)

        i = len(self.heap)
        parent = i // 2

        while i > 1 and self.heap[parent - 1] < self.heap[i - 1]:
            self.heap[parent - 1], self.heap[i - 1] = self.heap[i - 1], self.heap[parent - 1]
            i = parent
            parent = i // 2

    def _heapify(self, idx):
        largest = idx
        left = (idx * 2) + 1
        right = (idx * 2) + 2

        if left >= len(self.heap):
            return
        elif right < len(self.heap):
            if self.heap[largest] < self.heap[right]:
                largest, right = right, largest

        if self.heap[largest] < self.heap[left]:
            largest, left = left, largest
        if largest != idx:
            self.heap[idx], self.heap[largest] = self.heap[largest], self.heap[idx]
            self._heapify(largest)

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
    min_heap = MaxHeap()
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
    test_arr = MaxHeap(test_arr)
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

# [37, 11, 22, 5, 4, 7, 10, 1]
# 37
# 22
# 11
# 10
# [57, 5, 7, 1, 2, 4]
# 57
# 7
# 5
# -------------------------------------
# [45, 33, 22, 15, 4, 9, 7, 2, 5]
# 45
# 33
# 22
# 81
# 15
# [13, 7, 9, 5, 4, 2]
