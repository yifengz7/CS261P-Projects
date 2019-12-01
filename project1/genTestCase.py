import random
import pickle

l = 1000
r = 10*l

k = random.sample(range(l * 100), r)
v = random.sample(range(l * 100), r)

with open("data.pickle", "wb") as f:
    pickle.dump((l, r, k, v), f)
with open("data.pickle", "rb") as f:
    print(pickle.load(f))
