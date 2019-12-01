from BinHeap import *
from FibHeap import *

from matplotlib import pyplot as plt
import random
import time


def test_bin_heap(array, k):
    start = time.time()
    heap = BinaryHeap()
    for i in range(k):
        heap.push(array[i])
    for i in range(k, len(array)):
        val = array[i]
        if val > heap.min:
            heap.pop()
            heap.push(val)
    end = time.time()
    return end - start

def test_fib_heap(array, k):

    start = time.time()
    heap = FibHeap(0, 0)
    for i in range(k):
        heap.insert(FibheapNode(array[i]))
    for i in range(k, len(array)):
        val = array[i]
        if val > heap.find_min().key:
            heap.delete_min()
            heap.insert(FibheapNode(val))
    end = time.time()
    return end - start


ns = [10, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000, 500000, 1000000]
percentage = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]


for n in ns:
    xs = []
    y1 = []
    y2 = []
    for p in percentage:
        array = random.sample(range(0, n * 100), n)
        k = int(n * p)
        xs.append(k)
        a = test_bin_heap(array, k)
        y1.append(a)
        b = test_fib_heap(array, k)
        y2.append(b)

    l1 = plt.plot(xs, y1, "r")
    l2 = plt.plot(xs, y2, "g")
    plt.legend(handles=[l1[0], l2[0]], labels=["Binary Heap", "Fibonacci Heap"])
    plt.title(f"n={n}")
    plt.xlabel("k")
    plt.ylabel("time")
    plt.savefig(f"figures_new/{n}.png")
    plt.clf()

