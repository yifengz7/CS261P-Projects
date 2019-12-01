from cuckooHashTable import *
import matplotlib.pyplot as plt
import time
import math
import pickle


with open("data.pickle", "rb") as f:
    l, r, k, v = pickle.load(f)
tb = CuckooHashTable(l)

time_set = [0]

lf = []
time_search = [0]

ct = 0

for i in range(r):
    if i % 1000 == 0:
        print(i)

    start = time.time()
    ret = tb.set(k[i], v[i])
    end = time.time()
    set_time = end - start
    time_set.append(set_time + time_set[-1])

    start = time.time()
    tb.search(k[i])
    end = time.time()
    search_time = end - start
    time_search.append(search_time + time_search[-1])

    load_factor = tb.get_load_factor()
    lf.append(load_factor)

plt.plot(lf, [math.log(i) for i in time_set[1:]])
plt.title("Set for Cuckoo Hashing")
plt.xlabel("Load Factor")
plt.ylabel("Logarithm of Cumulative Time")
plt.savefig("cuckoo_set.png")
plt.show()


plt.plot(lf, [math.log(i) for i in time_search[1:]])
plt.title("Search for Cuckoo Hashing")
plt.xlabel("Load Factor")
plt.ylabel("Logarithm of Cumulative Time")
plt.savefig("cuckoo_search.png")
plt.show()


