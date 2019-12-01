from chainedHashTable import *
import matplotlib.pyplot as plt
import time
import pickle


with open("data.pickle", "rb") as f:
    l, r, k, v = pickle.load(f)
tb = ChainedHashTable(l)

time_set = [0]

lf = []
time_search = [0]

ct = 0

for i in range(r):
    start = time.time()
    ret = tb.set(k[i], v[i])
    end = time.time()
    set_time = end - start
    time_set.append(set_time + time_set[-1])
    # if insertion was successful

    start = time.time()
    tb.search(k[i])
    end = time.time()
    search_time = end - start
    time_search.append(search_time + time_search[-1])

    load_factor = tb.get_load_factor()
    lf.append(load_factor)

plt.plot(lf, time_set[1:])
plt.title("Set for Chained Hashing")
plt.xlabel("Load Factor")
plt.ylabel("Cumulative Time")
plt.savefig("chained_set.png")
plt.show()


plt.plot(lf, time_search[1:])
plt.title("Search for Chained Hashing")
plt.xlabel("Load Factor")
plt.ylabel("Cumulative Time")
plt.savefig("chained_search.png")
plt.show()


