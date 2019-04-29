class MaxPriorityQueue:
    # A Priority Queue where the maximum element is removed first.
    # Implemented using a Heap.
    # TODO Add in place heap creation.
    def __init__(self):
        self.heap = []
        self.size = 0

    def insert_max(self, value):
        self.heap.append(value)
        self.bubble_up_max(len(self.heap)-1)

    def extract_max(self):
        value = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop(len(self.heap) - 1)
        self.bubble_down_max(0)
        return value

    def bubble_up_max(self, index):
        currentIndex = index
        while self.get_parent(currentIndex) != -1:
            parent = self.get_parent(currentIndex)
            if self.heap[parent] < self.heap[currentIndex]:
                temp = self.heap[parent]
                self.heap[parent] = self.heap[currentIndex]
                self.heap[currentIndex] = temp
                currentIndex = parent
            else:
                currentIndex = -1

    def bubble_down_max(self, index):
        left = self.get_left(index)
        right = self.get_right(index)
        largest = -1
        if left != -1 and right != -1:
            if self.heap[left] > self.heap[right]:
                largest = left
            else:
                largest = right
        elif right != -1:
            if self.heap[right] > self.heap[index]:
                largest = right
        elif left != -1:
            if self.heap[left] > self.heap[index]:
                largest = left
        if largest != -1 and self.heap[largest] > self.heap[index]:
            self.swap(index, largest)
            self.bubble_down_max(largest)

    def swap(self, index1, index2):
        temp = self.heap[index1]
        self.heap[index1] = self.heap[index2]
        self.heap[index2] = temp

    def get_parent(self, index):
        parent = index//2
        if index == 0:
            return -1
        return parent

    def get_right(self, index):
        right = 2*index + 1
        if right >= len(self.heap):
            return -1
        return right

    def get_left(self, index):
        left = 2*index
        if left >= len(self.heap):
            return -1
        return left

    def getLayerOfElement(self, n):
        counter = 1
        currentLayer = 0
        while(True):
            if(counter >= n):
                return currentLayer
            currentLayer += 1
            counter = counter*2


class MinPriorityQueue:
    # A Priority Queue where the minimum element is removed first.
    # Implemented using a Heap.
    # TODO Add in place heap creation.
    def __init__(self):
        self.heap = []
        self.size = 0

    def insert_min(self, value):
        self.heap.append(value)
        self.bubble_up_min(len(self.heap)-1)

    def extract_min(self):
        self.size += 1
        value = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop(len(self.heap) - 1)
        self.bubble_down_min(0)
        return value

    def bubble_up_min(self, index):
        currentIndex = index
        while self.get_parent(currentIndex) != -1:
            parent = self.get_parent(currentIndex)
            if self.heap[parent] > self.heap[currentIndex]:
                temp = self.heap[parent]
                self.heap[parent] = self.heap[currentIndex]
                self.heap[currentIndex] = temp
                currentIndex = parent
            else:
                currentIndex = -1

    def bubble_down_min(self, index):
        left = self.get_left(index)
        right = self.get_right(index)
        smallest = -1
        if left != -1 and right != -1:
            if self.heap[left] < self.heap[right]:
                smallest = left
            else:
                smallest = right
        elif right != -1:
            if self.heap[right] < self.heap[index]:
                smallest = right
        elif left != -1:
            if self.heap[left] < self.heap[index]:
                smallest = left
        if smallest != -1 and self.heap[smallest] < self.heap[index]:
            self.swap( index, smallest)
            self.bubble_down_min(smallest)
    
    def swap(self, index1, index2):
        temp = self.heap[index1]
        self.heap[index1] = self.heap[index2]
        self.heap[index2] = temp

    def get_parent(self, index):
        parent = index//2
        if index == 0:
            return -1
        return parent

    def get_right(self, index):
        right = 2*index + 1
        if right >= len(self.heap):
            return -1
        return right

    def get_left(self, index):
        left = 2*index
        if left >= len(self.heap):
            return -1
        return left

    def getLayerOfElement(self, n):
        counter = 1
        currentLayer = 0
        while(True):
            if(counter >= n):
                return currentLayer
            currentLayer += 1
            counter = counter*2