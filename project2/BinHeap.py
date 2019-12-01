class BinaryHeap:
    def __init__(self):
        self.__heap = []
        self.__last_index = -1

    def push(self, value):
        self.__last_index += 1
        if self.__last_index < len(self.__heap):
            self.__heap[self.__last_index] = value
        else:
            self.__heap.append(value)
        self.__siftup(self.__last_index)

    def pop(self):
        if self.__last_index == -1:
            raise IndexError('pop from empty heap')

        min_value = self.__heap[0]

        self.__heap[0] = self.__heap[self.__last_index]
        self.__last_index -= 1
        self.__siftdown(0)

        return min_value

    @property
    def min(self):
        return self.__heap[0]

    def __siftup(self, index):
        while index > 0:
            parent_index, parent_value = self.__get_parent(index)

            if parent_value <= self.__heap[index]:
                break

            self.__heap[parent_index], self.__heap[index] =\
                self.__heap[index], self.__heap[parent_index]

            index = parent_index

    def __siftdown(self, index):
        while True:
            index_value = self.__heap[index]

            left_child_index, left_child_value = self.__get_left_child(index, index_value)
            right_child_index, right_child_value = self.__get_right_child(index, index_value)

            if index_value <= left_child_value and index_value <= right_child_value:
                break

            if left_child_value < right_child_value:
                new_index = left_child_index
            else:
                new_index = right_child_index

            self.__heap[new_index], self.__heap[index] =\
                self.__heap[index], self.__heap[new_index]

            index = new_index

    def __get_parent(self, index):
        if index == 0:
            return None, None

        parent_index = (index - 1) // 2

        return parent_index, self.__heap[parent_index]

    def __get_left_child(self, index, default_value):
        left_child_index = 2 * index + 1

        if left_child_index > self.__last_index:
            return None, default_value

        return left_child_index, self.__heap[left_child_index]

    def __get_right_child(self, index, default_value):
        right_child_index = 2 * index + 2

        if right_child_index > self.__last_index:
            return None, default_value

        return right_child_index, self.__heap[right_child_index]

    def __len__(self):
        return self.__last_index + 1

    def __str__(self):
        return str(self.__heap)

    def __repr__(self):
        return str(self)

if __name__ == "__main__":
    h = BinaryHeap()
    for i in range(10):
        h.push(i)
        print(h)
    while h:
        print(h.pop())
