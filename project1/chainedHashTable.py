from randomUtils import *


class Node:
    def __init__(self, key: int = None, val: int = None):
        self.key = key
        self.val = val
        self.next = None

    def __str__(self):
        return f"({self.key}, {self.val})"


class ChainedHashTable:

    def __init__(self, length: int):
        self.array = [Node() for _ in range(length)]
        self.length = length
        self.num_items = 0
        self.h = lambda x: x % length

    def get_load_factor(self):
        return self.num_items / self.length

    def __str__(self):
        s = ""
        for i in range(self.length):
            s += f"[{i}]"
            it = self.array[i]
            while it:
                if it.val is None:
                    s += "head->"
                else:
                    s += str(it) + "->"
                it = it.next
            s += "end"
            s += "\n"
        return s

    def set(self, key: int, val: int):
        index = self.h(key)
        it = self.array[index]
        while it.next:
            it = it.next
        it.next = Node(key, val)
        self.num_items += 1
        return 0

    def search(self, key: int):
        index = self.h(key)
        it = self.array[index]
        while it:
            if it.key == key:
                return it.val
            it = it.next
        return False
